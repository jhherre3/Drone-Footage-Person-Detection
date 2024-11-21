# Drone-Footage-Person-Detection

Drone-Footage-Person-Detection is a Python-based project designed to analyze drone footage and detect people using the YOLOv5 object detection model. The program processes video files, identifies people in the frames, and highlights them with bounding boxes, providing a powerful tool for analyzing aerial footage for human presence.

---

## Features
- **YOLOv5 Integration**: Utilizes a pretrained YOLOv5 model for high-accuracy object detection.
- **Real-Time Video Analysis**: Processes video frames, detects people, and adds bounding boxes with confidence scores.
- **Output Video Generation**: Saves a new video file with all detected objects highlighted.
- **Interactive Display**: View detection in real time while processing.
- **Customizable Detection Thresholds**: Adjust confidence thresholds for detecting objects.

---

## Requirements
- Python 3.8+
- OpenCV
- PyTorch
- YOLOv5 (via `torch.hub`)

---

## Installation
1. Clone this repository

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a YOLOv5-supported video file to analyze.

---

## Usage
1. Place your video file in the desired directory.
2. Update the `video_path` variable in `main.py` with the path to your video file.
3. Run the program:
    ```bash
    python main.py
    ```
4. View the output video in the specified output directory.

---

## How It Works
1. **Model Setup**: 
   - Loads the YOLOv5 model pretrained on the COCO dataset.
   - Uses the `torch.hub` utility to fetch the model directly from YOLOv5's repository.

2. **Video Analysis**: 
   - Reads frames from the input video using OpenCV.
   - Converts frames from BGR to RGB format for YOLOv5 processing.
   - Performs detection on each frame and filters results to include only "person" objects with a confidence score above 50%.

3. **Visualization**: 
   - Draws bounding boxes and confidence scores on detected persons in each frame.
   - Saves a new video with highlighted detections to the output directory.

4. **Real-Time Display**: 
   - Displays the processed frames in a window while allowing the user to quit by pressing 'q'.

---

## Output
- The processed video with detected people highlighted will be saved to the output directory.
- The file is uniquely named based on the base name (`Drone_analysis`) and an incrementing number.

---

## Example
Original Video:

![Original Frame Example](example_images/original_frame.jpg)

Processed Video:

![Processed Frame Example](example_images/processed_frame.jpg)

---

## Customization
### Confidence Threshold:
Modify the following line to adjust the detection confidence:
```python
if detection['name'] == 'person' and detection['confidence'] > 0.5:
