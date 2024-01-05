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

def generate_messages_with_single_url(single_url, file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if not line.strip().startswith('//')]

    for url in urls:
        yield f"/imagine {single_url} {url}"

def minimize_discord():
    discord_windows = [window for window in gw.getAllWindows() if 'Discord' in window.title]
    if discord_windows:
        discord_window = discord_windows[0]
        discord_window.minimize()

def job(single_url, file_path):
    try:
        for message in generate_messages_with_single_url(single_url, file_path):
            send_message(message)
            random_delay = random.uniform(-1, 1)
            print(f"Random delay: {random_delay} seconds")
            time.sleep(3 + random_delay)
            if keyboard.is_pressed('esc'):
                print("Script stopped by user.")
                break
    except KeyboardInterrupt:
        print("Script interrupted.")

    minimize_discord()


# Provide the single URL and the path to the list of URLs
single_url = 'https://cdn.discordapp.com/ephemeral-attachments/1062880104792997970/1189827700542685265/1769538_orig.jpg?ex=659f9465&is=658d1f65&hm=513a353910e0b295cb92ccef1ebc7655440c4f74e471d05e08d28ad6841d9b35&'
url_list_file_path = '231227_list.txt'

# Run the job function with the specified URL and file
job(single_url, url_list_file_path)
