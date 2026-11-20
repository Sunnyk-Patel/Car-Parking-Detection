# Car Parking Detection Using Python and OpenCV

## Overview

This project detects available and occupied parking spaces from a parking lot video using Python and OpenCV.

The application allows the user to mark individual parking spaces on a reference image. These coordinates are saved and then used to check the occupancy of each space while processing the video.

## Features

- Manual selection of parking spaces.
- Removal of incorrectly selected spaces.
- Saving and loading parking-space coordinates.
- Detection of occupied and available parking spaces.
- Visual representation using green and red rectangles.
- Display of the available parking-space count.

## Technologies

- Python
- OpenCV
- NumPy
- Pickle

## How the Project Works

The parking video is processed frame by frame. Each frame is converted into grayscale and passed through Gaussian blur and adaptive thresholding. Median filtering and dilation are then applied.

The processed image is divided into the previously selected parking regions. The number of non-zero pixels in each region is calculated and compared with a threshold to determine whether the space is occupied.

## Installation

Clone the repository:

```bash
git clone https://github.com/Sunnyk-Patel/Car-Parking-Detection.git
cd Car-Parking-Detection
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows, use:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

First, open the parking-space selection tool:

```bash
python CarParkingPicker.py
```

Controls:
- Left-click: Add a parking space.
- Right-click: Remove a parking space.
- Q: Exit.

The selected coordinates are saved in `data/CarParkPos`.

Start the detection application:

```bash
python main.py
```

Press Q to close the application.

## Project Structure

```text
Car-Parking-Detection/
├── assets/
├── data/
├── screenshots/
├── main.py
├── CarParkingPicker.py
├── requirements.txt
└── README.md
```

## Current Limitations

- The detection threshold may need adjustment under different lighting conditions.
- The current implementation uses image-processing techniques rather than a trained vehicle-detection model.
- Parking-space coordinates are configured manually for the reference parking lot.
- Detection performance depends on the camera angle and video quality.

## Future Improvements

- Test the application with different parking lot videos.
- Improve detection under changing lighting conditions.
- Add support for live camera input.
- Explore deep-learning-based vehicle detection.

## Author

Sunny Patel

GitHub: https://github.com/Sunnyk-Patel
