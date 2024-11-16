import pyautogui
import time
from PIL import ImageGrab


# Coordinates of a Bird when it hit the dinosaur
# You must start the game, and let a dinosaur hit a Bird
# Then get coordinate by running the code

def get_position():
    print("Now position the cursor at the top-left of bird and press Enter...")
    input("Ready? ")
    bird_top_left = pyautogui.position()  # Get top-left of Bird
    print("Bird Top-Left:", bird_top_left)

    print("Now position the cursor at the bottom-right of bird and press Enter...")
    input("Ready? ")
    bird_bottom_right = pyautogui.position()  # Get bottom-right of Bird
    print("Bird Bottom-Right:", bird_bottom_right)

    # Print positions for verification
    print(f"Bird area: {bird_top_left} to {bird_bottom_right}")

    # Go to the game browser within 3 sec
    time.sleep(3)

    # Capture the Bird area
    bird_image = ImageGrab.grab(
        bbox=(bird_top_left[0], bird_top_left[1], bird_bottom_right[0], bird_bottom_right[1]))
    bird_image.show()


get_position()
