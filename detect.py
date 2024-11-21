import os
import cv2
import torch
from config import VIDEO_PATH, OUTPUT_DIR, OUTPUT_BASE_NAME, CONFIDENCE_THRESHOLD

# Load the YOLOv5 model (pretrained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Function to generate a unique output filename
def get_unique_filename(base_path, base_name):
    num = 1
    while True:
        filename = f"{base_name}_{num}.mp4"
        output_path = os.path.join(base_path, filename)
        if not os.path.exists(output_path):
            return output_path
        num += 1

# Video processing function
def process_video(video_path, output_dir, base_name):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Cannot open video file {video_path}")
        return

    # Video properties
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Generate unique output path
    output_path = get_unique_filename(output_dir, base_name)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLOv5 expects RGB frames
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform detection
        results = model(rgb_frame)
        detections = results.pandas().xyxy[0]

        # Process detections
        for _, detection in detections.iterrows():
            if detection['name'] == 'person' and detection['confidence'] > CONFIDENCE_THRESHOLD:
                xmin, ymin, xmax, ymax = int(detection['xmin']), int(detection['ymin']), int(detection['xmax']), int(detection['ymax'])
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                label = f"Person: {detection['confidence']:.2f}"
                cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        out.write(frame)
        cv2.imshow('YOLOv5 Person Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")

if __name__ == "__main__":
    process_video(VIDEO_PATH, OUTPUT_DIR, OUTPUT_BASE_NAME)
