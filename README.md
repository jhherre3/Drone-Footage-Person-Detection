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

# Instructions for Using Template

This guide provides step-by-step instructions on how to use the YOLOv5 Person Detection program.

---

## Quick Start 

1. **Download the ZIP File**:
   - Go to the repository on GitHub.
   - Click the green **Code** button and select **Download ZIP**.
   - Extract the ZIP file to a folder on your computer.

2. **Open the Project in PyCharm**:
   - Launch PyCharm.
   - Click **File > Open**.
   - Select the folder where you extracted the ZIP file.

3. **Install Required Libraries**:
   - Open the terminal in PyCharm (bottom of the window).
   - Run:
     ```bash
     pip install -r requirements.txt
     ```

4. **Edit the Configuration**:
   - Open the `config.py` file in PyCharm.
   - Update the following:
     - `VIDEO_PATH`: Path to your input video.
     - `OUTPUT_DIR`: Directory to save processed videos.
     - (Optional) Adjust the `CONFIDENCE_THRESHOLD` if needed.

5. **Run the Detection**:
   - Right-click on `detect.py` in the PyCharm project view.
   - Select **Run 'detect'**.
   - The program will process your video and save the output in the directory specified in `OUTPUT_DIR`.

---

## Troubleshooting
- If you see errors related to missing packages, make sure you installed dependencies with:
  ```bash
  pip install -r requirements.txt

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

## Customization
### Confidence Threshold:
Modify the following line to adjust the detection confidence:
```python
if detection['name'] == 'person' and detection['confidence'] > 0.5:
