
# Car Parking Detection System

A computer vision-based parking space detection system built using Python and OpenCV. The application processes a parking lot video, identifies occupied and available parking spaces, and displays the available parking count in real time.

## Features

- Detects occupied and available parking spaces.
- Displays free parking spaces using green rectangles.
- Displays occupied parking spaces using red rectangles.
- Shows the number of available parking spaces.
- Allows users to select and remove parking spaces manually.
- Saves parking-space coordinates for future use.
- Automatically restarts the video when it reaches the end.

## Technologies Used

- Python
- OpenCV
- NumPy
- Pickle

## Project Structure

```text
Car-Parking-Detection/
├── assets/
│   ├── carPark.mp4
│   └── carParkImg.png
├── data/
│   └── CarParkPos
├── main.py
├── CarParkingPicker.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sunnyk-Patel/Car-Parking-Detection.git
```

2. Navigate to the project directory:

```bash
cd Car-Parking-Detection
```

3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the environment on macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

5. Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Select Parking Spaces

Run the parking-space picker:

```bash
python CarParkingPicker.py
```

- Left-click to add a parking space.
- Right-click to remove a parking space.
- Press Q to exit.

The coordinates are saved automatically in `data/CarParkPos`.

### Step 2: Run Car Parking Detection

Run the main application:

```bash
python main.py
```

Press Q to close the detection window.

## How It Works

1. OpenCV reads frames from the parking lot video.
2. Each frame is converted into grayscale.
3. Gaussian blur and adaptive thresholding are applied.
4. Image processing operations help identify occupied regions.
5. Each selected parking space is checked using its non-zero pixel count.
6. The application marks spaces as available or occupied and updates the count.

## Requirements

- Python 3
- OpenCV
- NumPy
- A compatible desktop environment supporting OpenCV display windows.

## Future Improvements

- Improve detection accuracy under different lighting conditions.
- Add vehicle detection using deep learning.
- Develop a graphical dashboard for parking management.
- Support live camera feeds.

## Author

Sunny Patel

GitHub: https://github.com/Sunnyk-Patel
