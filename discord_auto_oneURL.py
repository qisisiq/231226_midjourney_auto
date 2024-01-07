import time
import pyautogui
import pygetwindow as gw
import itertools
import random
import keyboard

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


def send_message(command, image_urls):
    if focus_discord():
        # Calculate the position of the chat box after ensuring Discord is focused
        screen_width, screen_height = pyautogui.size()
        chat_input_x = screen_width * 0.5  # 50% of the screen width
        chat_input_y = screen_height * 0.914  # 91.4% of the screen height
        
        # Move the mouse to the chat input area and click
        pyautogui.click(chat_input_x, chat_input_y)
        time.sleep(0.5)  # Short delay to ensure the click is registered
        
        # Type the /imagine command and press "Enter"
        pyautogui.typewrite(command)
        pyautogui.press('enter')
        time.sleep(1)  # Wait for Discord to process the command

        # Now type the image URLs and press "Enter"
        pyautogui.typewrite(image_urls)
        pyautogui.press('enter')
    else:
        print(f"Skipped message: {command} {image_urls}")

def generate_messages_with_single_url(single_url, file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if not line.strip().startswith('//')]

    for url in urls:
        # Only return the image URL part, since the command part is handled separately
        yield f"{single_url} {url}"

def minimize_discord():
    discord_windows = [window for window in gw.getAllWindows() if 'Discord' in window.title]
    if discord_windows:
        discord_window = discord_windows[0]
        discord_window.minimize()

def job(command, single_url, file_path):
    try:
        message_count = 0
        for message in generate_messages_with_single_url(single_url, file_path):
            send_message(command, message)
            message_count += 1
            
            # Check if 20 messages have been sent
            if message_count % 20 == 0:
                print("Sent 20 messages, waiting for 5 minutes...")
                time.sleep(300)  # Wait for 5 minutes

            # Wait for 3 seconds plus a random amount of time between -1 and 1 seconds
            random_delay = random.uniform(-1, 1)
            print(f"Random delay: {random_delay} seconds")
            time.sleep(3 + random_delay)

            # Check if the 'esc' key was pressed
            if keyboard.is_pressed('esc'):
                print("Script stopped by user.")
                break
    except KeyboardInterrupt:
        print("Script interrupted.")

    minimize_discord()


# Provide the single URL and the path to the list of URLs
command = '/imagine'
single_url = 'https://i.imgur.com/xdk7Xau.png'
url_list_file_path = '240105_seed_images_github_list.txt'

# Run the job function with the specified URL and file
job(command, single_url, url_list_file_path)
