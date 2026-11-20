
import cv2
import pickle
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "assets" / "carParkImg.png"
POSITIONS_PATH = BASE_DIR / "data" / "CarParkPos"

# Parking space dimensions
WIDTH, HEIGHT = 107, 48


def load_positions():
    try:
        with POSITIONS_PATH.open("rb") as file:
            positions = pickle.load(file)
        return positions if isinstance(positions, list) else []
    except FileNotFoundError:
        return []
    except (pickle.UnpicklingError, EOFError) as error:
        print(f"Could not read CarParkPos: {error}")
        return []


pos_list = load_positions()


def save_positions():
    """Save parking coordinates safely."""
    POSITIONS_PATH.parent.mkdir(parents=True, exist_ok=True)

    temp_path = POSITIONS_PATH.with_name(
        POSITIONS_PATH.name + ".tmp"
    )

    with temp_path.open("wb") as file:
        pickle.dump(pos_list, file)

    temp_path.replace(POSITIONS_PATH)


def mouse_click(event, x, y, flags, params):
    global pos_list

    if event == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((int(x), int(y)))
        save_positions()

        print(
            f"Added parking space at ({x}, {y}). "
            f"Total: {len(pos_list)}"
        )

    elif event == cv2.EVENT_RBUTTONDOWN:
        for index in range(len(pos_list) - 1, -1, -1):
            px, py = pos_list[index]

            if px <= x <= px + WIDTH and py <= y <= py + HEIGHT:
                removed = pos_list.pop(index)
                save_positions()

                print(
                    f"Removed parking space at {removed}. "
                    f"Total: {len(pos_list)}"
                )
                break


def main():
    if not IMAGE_PATH.is_file():
        print(f"Error: parking image not found: {IMAGE_PATH}")
        return

    image = cv2.imread(str(IMAGE_PATH))

    if image is None:
        print(f"Error: OpenCV could not read {IMAGE_PATH}")
        return

    print("Left-click: Add parking space")
    print("Right-click: Remove parking space")
    print("Q: Quit")

    window_name = "Parking Space Picker"

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_click)

    while True:
        display = image.copy()

        for x, y in pos_list:
            cv2.rectangle(
                display,
                (int(x), int(y)),
                (int(x) + WIDTH, int(y) + HEIGHT),
                (255, 0, 255),
                2
            )

        cv2.putText(
            display,
            f"Spaces: {len(pos_list)} | Left: Add | Right: Remove | Q: Quit",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 255),
            2,
            cv2.LINE_AA
        )

        cv2.imshow(window_name, display)

        if cv2.waitKey(20) & 0xFF in (ord("q"), ord("Q")):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
