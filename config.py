import os

# Configuration file for directories and settings

# Path to the video file (Update this path)
VIDEO_PATH = "your_video_path_here.mkv"

# Output directory for processed videos (Update this directory)
OUTPUT_DIR = "output_videos"

# Base name for output video
OUTPUT_BASE_NAME = "Drone_analysis"

# Confidence threshold for detections
CONFIDENCE_THRESHOLD = 0.5

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)
