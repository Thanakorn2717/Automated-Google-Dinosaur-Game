import pyautogui
import time
from PIL import ImageGrab


# Coordinates of a Cacti when it hit the dinosaur
# You must start the game, and let a dinosaur hit a Cacti
# Then get coordinate by running the code

def get_position():
    print("Position the cursor at the top-left of cacti and press Enter...")
    input("Ready? ")
    cacti_top_left = pyautogui.position()  # Get top-left of the Cacti
    print("Cacti Top-Left:", cacti_top_left)

    print("Now position the cursor at the bottom-right of cacti and press Enter...")
    input("Ready? ")
    cacti_bottom_right = pyautogui.position()  # Get bottom-right of the Cacti
    print("Cacti Bottom-Right:", cacti_bottom_right)

    # Print positions for verification
    print(f"Cacti area: {cacti_top_left} to {cacti_bottom_right}")

    # Go to the game browser within 3 sec
    time.sleep(3)

    # Capture the Cacti area
    cacti_image = ImageGrab.grab(
        bbox=(cacti_top_left[0], cacti_top_left[1], cacti_bottom_right[0], cacti_bottom_right[1]))
    cacti_image.show()


get_position()
