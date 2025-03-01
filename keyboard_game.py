#Max H, Keyboard Game, (FYI you may need to download the keyboard module using "pip install keyboard" inside the terminal if you do not do this the code will not run), you will also need to import time

import keyboard
import time

#This is the entire spacebar presses game
def spacebar_per_seconds_game():
    length = 15
    start_time = time.time()
    end_time = start_time + length
    print(f"You have {length} seconds to spam the spacebar!")

    total_spacebar_presses = 0
    space_pressed = False

    time.sleep(2)
    for i in range(4,1):
        print(f"{i}")
        time.sleep(1)
    print("Begin!")

    while time.time() < end_time: # If the current time is less than the ending time
        if keyboard.is_pressed('space'):
            if not space_pressed:  # Only count if it wasn't pressed before
                total_spacebar_presses += 1
                space_pressed = True  # Set the flag to True
        else:
            space_pressed = False  # Reset the flag when space is released
        
    print("\nFinished!")
    print(f"Here was your total presses!: {total_spacebar_presses}")
    return total_spacebar_presses