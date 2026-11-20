CAR PARKING DETECTION PROJECT

1. Open this folder in VS Code.
2. Open Terminal > New Terminal.
3. Create and activate a virtual environment (macOS):
     python3 -m venv .venv
     source .venv/bin/activate
4. Install libraries:
     python -m pip install -r requirements.txt
5. Run the parking-space picker if you want to edit parking positions:
     python CarParkingPicker.py
   Left-click adds a space, right-click removes a space, Q exits.
6. Run the detection program:
     python main.py
   Press Q to exit.

IMPORTANT:
- cvzone is no longer required.
- Keep carPark.mp4, carParkImg.png and CarParkPos in this same folder.
- The detection threshold (900) may need tuning for different lighting/video.
