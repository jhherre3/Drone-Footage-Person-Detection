# Instructions for Using YOLOv5 Person Detection Template

This guide provides step-by-step instructions on how to use the YOLOv5 Person Detection program. Follow the method that best suits your experience level.

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
