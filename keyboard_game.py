#Max H, Keyboard Game, (FYI you may need to download the keyboard module using "pip install keyboard" inside the terminal if you do not do this the code will not run), you will also need to import time

import keyboard

import time

def spacebar_per_seconds_game():
    total_time = 15.00
    total_time = float(total_time)
    print(f"This is the total time you have to press the spacebar: {total_time}")
    total_spacebar_presses = 0
    time.sleep(3)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Begin!")
    while total_time > 0:
        if keyboard.is_pressed("Spacebar"):
            time.sleep(0.01)
            total_spacebar_presses += 1
        time.sleep(0.01)
        total_time = total_time - 0.01
    total_spacebar_presses = round(total_spacebar_presses, 0)
    total_spacebar_presses = int(total_spacebar_presses)
    print("Finished!")
    print(f"Here was your total presses!: {total_spacebar_presses}")
    return total_spacebar_presses

spacebar_per_seconds_game()