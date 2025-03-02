#Max H, Keyboard Game, (FYI you may need to download the keyboard module using "pip install keyboard" inside the terminal if you do not do this the code will not run), you will also need to import time

import keyboard
import time

#This is the entire spacebar presses game
def spacebar_per_seconds_game():
    length = 60
    start_time = time.time()
    end_time = start_time + length
    print(f"\033cYou have {length} seconds to spam the spacebar!")

    total_spacebar_presses = 0
    space_pressed = False

    time.sleep(1.5)
    for i in range(4,1):
        print(f"{i}")
        time.sleep(1)
    print(f"Begin!\n{length} Second(s) remaining!",end='   ')

    while time.time() < end_time: # If the current time is less than the ending time
        remaining_time = round(end_time - time.time(),1)
        if keyboard.is_pressed('space'):
            if not space_pressed:  # Only count if it wasn't pressed before
                total_spacebar_presses += 1
                space_pressed = True  # Set the flag to True
        else:
            space_pressed = False  # Reset the flag when space is released
        
        if remaining_time <= 5:
            if remaining_time % 1 == 0:
                print(f"\r{int(remaining_time)} Second(s) remaining!",end='   ')
        else:
            if remaining_time % 5 == 0:
                print(f"\r{int(remaining_time)} Second(s) remaining!",end='   ')
        
        
    print("\033cFinished!")
    print(f"Here was your total presses!: {total_spacebar_presses}")
    return total_spacebar_presses