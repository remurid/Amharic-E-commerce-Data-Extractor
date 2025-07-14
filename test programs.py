import pyautogui
import random
import time

# --- Configuration ---

# Time intervals for short, random actions (in seconds)
SHORT_ACTION_MIN_INTERVAL = 1
SHORT_ACTION_MAX_INTERVAL = 12

# Time intervals for switching tabs in an application like VS Code (in seconds)
# 3 minutes = 180 seconds, 15 minutes = 900 seconds
TAB_SWITCH_MIN_INTERVAL = 180
TAB_SWITCH_MAX_INTERVAL = 900

# Get screen dimensions for realistic mouse movement
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

# List of keyboard keys that won't affect a document
SAFE_KEYS = [
    'up', 'down', 'left', 'right',  # Arrow keys
    'ctrlleft', 'ctrlright',        # Control keys
    'altleft', 'altright',          # Alt keys
    'shiftleft', 'shiftright'       # Shift keys
]

# --- Main Script ---

def perform_random_action():
    """Chooses and performs a random, small, human-like action."""
    
    action = random.choice(['move', 'click', 'scroll', 'press_key'])

    if action == 'move':
        # Move mouse to a random position on the screen over a random duration
        target_x = random.randint(0, SCREEN_WIDTH)
        target_y = random.randint(0, SCREEN_HEIGHT)
        duration = random.uniform(0.2, 1.5)  # Human-like movement speed
        pyautogui.moveTo(target_x, target_y, duration=duration)
        print(f"Action: Moved mouse to ({target_x}, {target_y}) over {duration:.2f}s")

    elif action == 'click':
        # Perform a single click at the current mouse position
        pyautogui.click()
        print("Action: Clicked mouse")

    elif action == 'scroll':
        # Scroll up or down by a small, random amount
        scroll_amount = random.randint(-5, 5) * 10  # Small, noticeable scrolls
        pyautogui.scroll(scroll_amount)
        print(f"Action: Scrolled by {scroll_amount} units")

    elif action == 'press_key':
        # Press and release a random safe key
        key_to_press = random.choice(SAFE_KEYS)
        pyautogui.press(key_to_press)
        print(f"Action: Pressed '{key_to_press}' key")

def switch_vscode_tab():
    """Simulates switching tabs using Ctrl+Tab."""
    pyautogui.hotkey('ctrl', 'tab')
    print("\n--- Switched VS Code Tab ---\n")

# --- Main Loop ---

if __name__ == "__main__":
    print("Starting human-like activity simulator... Press Ctrl+C to stop.")
    
    # Initialize timers
    last_tab_switch_time = time.time()
    tab_switch_interval = random.uniform(TAB_SWITCH_MIN_INTERVAL, TAB_SWITCH_MAX_INTERVAL)

    try:
        while True:
            # Check if it's time to perform a long-interval action (tab switch)
            if time.time() - last_tab_switch_time > tab_switch_interval:
                switch_vscode_tab()
                # Reset the timer for the next tab switch
                last_tab_switch_time = time.time()
                tab_switch_interval = random.uniform(TAB_SWITCH_MIN_INTERVAL, TAB_SWITCH_MAX_INTERVAL)

            # Perform a short, random action
            perform_random_action()
            
            # Wait for a random interval before the next short action
            sleep_time = random.uniform(SHORT_ACTION_MIN_INTERVAL, SHORT_ACTION_MAX_INTERVAL)
            print(f"Next action in {sleep_time:.2f} seconds...\n")
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")