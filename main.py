import pyautogui
from PIL import ImageGrab, ImageOps
import time
import numpy as np

# Constants for detection distances
BEFORE_JUMP_DISTANCE = 80
BEFORE_DUCK_DISTANCE = 80

# Coordinates of a cacti and a bird when they hit the dinosaur
# These must be calibrated using get_position.py
cacti = (625, 297, 648, 333)  # Cacti's bounding box (top-left, bottom-right)
bird = (612, 266, 654, 299)  # Bird's bounding box (top-left, bottom-right)


def detect_obstacles(cacti, bird):
    print("Starting in 3 seconds...")  # Go to the game browser within 3 sec
    time.sleep(3)
    pyautogui.press("space")  # Start the game
    print("Running... Press Ctrl+C to stop.")

    while True:
        # **Cacti Detection**
        to_jump_area = ImageGrab.grab(
            bbox=(
                cacti[0] + BEFORE_JUMP_DISTANCE,  # Shifted by BEFORE_JUMP_DISTANCE
                cacti[1],
                cacti[2] + BEFORE_JUMP_DISTANCE,
                cacti[3]
            )
        )
        to_jump_area_gray = ImageOps.grayscale(to_jump_area)
        to_jump_pixel_sum = np.sum(np.array(to_jump_area_gray))

        # **Bird Detection**
        to_duck_area = ImageGrab.grab(
            bbox=(
                bird[0] + BEFORE_DUCK_DISTANCE,  # Shifted by BEFORE_DUCK_DISTANCE
                bird[1],
                bird[2] + BEFORE_DUCK_DISTANCE,
                bird[3]
            )
        )
        to_duck_area_gray = ImageOps.grayscale(to_duck_area)
        to_duck_pixel_sum = np.sum(np.array(to_duck_area_gray))

        # Debug: Print pixel sums for calibration
        print(f"to_jump_pixel_sum: {to_jump_pixel_sum}, to_duck_pixel_sum: {to_duck_pixel_sum}")

        # Thresholds for detecting obstacles
        jump_threshold = 200000  # Adjust based on cacti visuals
        duck_threshold = 300000  # Adjust based on bird visuals

        # Check if cacti are detected
        if to_jump_pixel_sum < jump_threshold:
            print("Cacti detected! Jumping...")
            pyautogui.press("space")
            time.sleep(0.1)  # Short delay to avoid multiple jumps

        # Check if bird is detected
        elif to_duck_pixel_sum < duck_threshold:
            print("Bird detected! Ducking...")
            pyautogui.keyDown("down")  # Press and hold the "down" key
            time.sleep(0.2)  # Keep it held for 1.5 seconds
            pyautogui.keyUp("down")  # Release the "down"  key
            time.sleep(0.1)  # Short delay to avoid redundant actions


if __name__ == "__main__":
    try:
        detect_obstacles(cacti, bird)
    except KeyboardInterrupt:
        print("\nGame automation stopped.")

# *** this version doesn't deal with acceleration increment ***

