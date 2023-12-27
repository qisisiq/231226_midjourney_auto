import time
import pyautogui
import pygetwindow as gw
import itertools
import random

def focus_discord():
    discord_windows = [window for window in gw.getAllWindows() if 'Discord' in window.title]
    if discord_windows:
        discord_window = discord_windows[0]  # Assume the first matching window is the one we want
        if not discord_window.isMaximized:
            discord_window.maximize()
        discord_window.activate()
        time.sleep(1)  # Wait for the window to focus
        return True
    else:
        print("Discord window not found. Please open Discord.")
        return False


def send_message(message):
    if focus_discord():
        # Calculate the position of the chat box after ensuring Discord is focused
        screen_width, screen_height = pyautogui.size()
        chat_input_x = screen_width * 0.5  # 50% of the screen width
        chat_input_y = screen_height * 0.914  # 91.4% of the screen height
        
        # Move the mouse to the chat input area and click
        pyautogui.click(chat_input_x, chat_input_y)
        time.sleep(0.5)  # Short delay to ensure the click is registered
        pyautogui.typewrite(message)
        pyautogui.press('enter')
    else:
        print(f"Skipped message: {message}")

def generate_url_pairs(file_path):
    with open(file_path, 'r') as file:
        # Filter out lines that start with '//' and strip whitespace
        urls = [line.strip() for line in file if not line.strip().startswith('//')]

    # Generate pairs using itertools.combinations
    for url1, url2 in itertools.combinations(urls, 2):
        yield f"/imagine {url1} {url2}"

def job():
    for message in generate_url_pairs('231226_image_list.txt'):
        send_message(message)
        # Wait for 20 seconds plus a random amount of time between -5 and 5 seconds
        time.sleep(20 + random.uniform(-5, 5))

# Run the job function directly
job()
