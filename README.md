# CatchingPoints
Welcome to CatchingPoints – a real-time, gesture-driven game powered by MediaPipe hand tracking. Join the fun, sharpen your reflexes, and help us make this project even better!

CatchingPoints challenges you to “grab” floating points on screen using only your hand gestures. Five blue targets appear at random locations; guide them into your hand’s yellow capture box and close your fingers to collect. When all targets disappear, you win!

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

## Contributing

If you think this is a game with great potential, or you want to tweak things a little, feel free!!! Your ideas and code can make CatchingPoints even more engaging! Whether it’s improving performance, adding new game modes, or enhancing visuals, we welcome:

Bug reports and feature requests via GitHub Issues

Pull requests with clear descriptions and examples

Discussion on optimizing hand-tracking thresholds or UI