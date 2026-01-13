<p align="center">
<h1 align="center">Object Detection with Voice Feedback
</h1>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Computer%20Vision-Real--Time-success">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?logo=opencv&logoColor=white">
  <img src="https://img.shields.io/badge/cvlib-Object%20Detection-0A66C2?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/YOLOv3-Deep%20Learning-FF6F00?logo=tensorflow&logoColor=white">
  <img src="https://img.shields.io/badge/gTTS-Text%20to%20Speech-4285F4?logo=google&logoColor=white">
</p>



<p align="center">
  <img src="./assets/object_detection.gif" alt="Watch the demo" width="800"/><br/>
  <em>Demo: Object Detection </em>
</p>

## 🎥 Real-Time Object Detection with Voice Feedback

This project implements a real-time object detection system using a webcam and deep learning, enhanced with audio feedback that verbally announces detected objects. It combines computer vision and text-to-speech technologies to create an interactive and accessible AI application.

## 📌 About the Project

The application captures live video from a webcam, detects common objects using a pre-trained YOLOv3 model via cvlib, and visually highlights them with bounding boxes. Once the detection session ends, the system generates a natural language sentence describing the detected objects and speaks the result aloud using text-to-speech.

This project demonstrates how computer vision outputs can be converted into human-friendly, multimodal feedback.

## ✨ Key Features

- Real-time webcam object detection

- YOLOv3 deep learning model (COCO dataset)

- Bounding box visualization

- Duplicate detection prevention

- Text-to-Speech output using gTTS

## 🛠️ Tech Stack

- Python – Core language used to implement the application logic

- OpenCV (cv2) – Webcam access, image processing, and video display

- cvlib – High-level wrapper for object detection using YOLO

- YOLOv3 – Pre-trained real-time object detection model

- COCO Dataset – Dataset used to train the YOLOv3 model for common objects

- gTTS (Google Text-to-Speech) – Converts detected object descriptions into speech

- playsound – Plays generated audio output

## 3. Installation and Setup Guide


### Step 1: Create and activate virtual environment
```bash
python3 -m venv .cvvenv
source .cvvenv/bin/activate
```

### Step 2: Install requirements

```bash
pip install -r requirements.txt
```

### Step 3: Run the python file

```bash
python3 main1.py
```