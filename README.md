# CatchingPoints
This is a game based on mediapipe and gesture recognition

There will be 5 points on the screen and you will have to "catch" the points on the screen

Place your hand over the blue points on the screen so that the blue point you want to capture is in the yellow box and close all your fingers to form a fist

The points will disappear as you "catch" them and if the points all disappears the game will exit and you win!!!

## Features
- Real-time hand tracking using MediaPipe
- Dynamic point generation
- Convex hull gesture detection
- Simple and intuitive gameplay

## Requirements
- Python 3.7+
- Webcam
- Required packages (see `requirements.txt`)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hand-point-catcher.git
   cd hand-point-catcher
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run:
    ```bash
    python catching_points.py
    ```