# Python - Generates a simple, animated loading bar in the console.

import time
import sys

def animated_loading_bar(duration, bar_length=40, fill_char='#', empty_char='-'):
    """
    Displays a simple animated loading bar in the console.

    Args:
        duration (int): The total duration of the loading bar in seconds.
        bar_length (int): The desired length of the loading bar in characters.
        fill_char (str): The character used to represent the filled portion of the bar.
        empty_char (str): The character used to represent the empty portion of the bar.
    """
    start_time = time.time()
    end_time = start_time + duration

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = min(elapsed_time / duration, 1.0)
        filled_length = int(bar_length * progress)
        bar = fill_char * filled_length + empty_char * (bar_length - filled_length)
        percentage = int(progress * 100)

        # Use carriage return to overwrite the current line
        sys.stdout.write(f'\rLoading: [{bar}] {percentage}%')
        sys.stdout.flush()
        time.sleep(0.05) # Small delay to control animation speed

    # Ensure the bar is fully complete at the end
    sys.stdout.write(f'\rLoading: [{fill_char * bar_length}] 100%\n')
    sys.stdout.flush()

if __name__ == "__main__":
    print("Starting simulation of a task...")
    animated_loading_bar(duration=5) # Simulate a 5-second task
    print("Task completed!")