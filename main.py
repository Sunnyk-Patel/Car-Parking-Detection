import cv2
import pickle
import numpy as np
from pathlib import Path

# Use paths relative to this script, so it works even when VS Code's
# current working directory is different.
BASE_DIR = Path(__file__).resolve().parent

VIDEO_PATH = BASE_DIR / "assets" / "carPark.mp4"
POSITIONS_PATH = BASE_DIR / "data" / "CarParkPos"

# Parking-space rectangle size (must match the picker).
WIDTH, HEIGHT = 107, 48


def load_positions():
    """Load the saved parking-space coordinates."""
    try:
        with POSITIONS_PATH.open("rb") as file:
            positions = pickle.load(file)
        if not isinstance(positions, list):
            raise ValueError("CarParkPos must contain a list of (x, y) coordinates.")
        return positions
    except FileNotFoundError:
        print(f"Error: parking positions file not found: {POSITIONS_PATH}")
        print("Run CarParkingPicker.py first, add parking spaces, and press Q to exit.")
        return []


def draw_label(image, text, origin, color, scale=0.55, thickness=2):
    """Draw readable text with a filled background (no cvzone dependency)."""
    x, y = origin
    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_w, text_h), baseline = cv2.getTextSize(text, font, scale, thickness)
    top = max(0, y - text_h - baseline - 6)
    right = min(image.shape[1] - 1, x + text_w + 8)
    cv2.rectangle(image, (x, top), (right, min(image.shape[0] - 1, y + 4)), color, -1)
    cv2.putText(image, text, (x + 4, y - 2), font, scale, (255, 255, 255),
                thickness, cv2.LINE_AA)


def check_parking_space(image, processed_image, positions):
    free_count = 0
    frame_h, frame_w = processed_image.shape[:2]

    for position in positions:
        if not isinstance(position, (tuple, list)) or len(position) != 2:
            continue

        x, y = map(int, position)

        # Ignore invalid coordinates instead of crashing on an empty crop.
        if x < 0 or y < 0 or x + WIDTH > frame_w or y + HEIGHT > frame_h:
            continue

        crop = processed_image[y:y + HEIGHT, x:x + WIDTH]
        count = cv2.countNonZero(crop)

        if count < 900:
            color = (0, 200, 0)       # Green = free
            thickness = 3
            free_count += 1
        else:
            color = (0, 0, 255)       # Red = occupied
            thickness = 2

        cv2.rectangle(image, (x, y), (x + WIDTH, y + HEIGHT), color, thickness)
        draw_label(image, str(count), (x, y + HEIGHT - 3), color, scale=0.42, thickness=1)

    draw_label(
        image,
        f"Free: {free_count}/{len(positions)}",
        (20, 42),
        (0, 150, 0),
        scale=0.9,
        thickness=2
    )


def main():
    if not VIDEO_PATH.is_file():
        print(f"Error: video file not found: {VIDEO_PATH}")
        return

    positions = load_positions()
    if not positions:
        print("No parking spaces loaded. Add spaces using CarParkingPicker.py.")
        return

    cap = cv2.VideoCapture(str(VIDEO_PATH))
    if not cap.isOpened():
        print(f"Error: OpenCV could not open the video: {VIDEO_PATH}")
        return

    print("Parking detection started. Press Q to quit.")

    try:
        while True:
            success, image = cap.read()

            # Restart the video at the end. If rewinding fails, stop safely.
            if not success:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                success, image = cap.read()
                if not success:
                    print("Error: unable to read video frames.")
                    break

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 1)
            threshold = cv2.adaptiveThreshold(
                blurred, 255,
                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV,
                25, 16
            )
            median = cv2.medianBlur(threshold, 5)
            kernel = np.ones((3, 3), np.uint8)
            dilated = cv2.dilate(median, kernel, iterations=1)

            check_parking_space(image, dilated, positions)
            cv2.imshow("Car Parking Detection", image)

            if cv2.waitKey(10) & 0xFF in (ord("q"), ord("Q")):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
