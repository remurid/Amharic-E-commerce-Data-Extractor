import pyautogui
import random
import time

# Configuration: ranges (in seconds and pixels)
MIN_SCROLL_INTERVAL = 0.5   # minimum time between scrolls (in seconds)
MAX_SCROLL_INTERVAL = 260  # maximum time between scrolls

MIN_SCROLL_AMOUNT = -300    # negative = scroll up, positive = scroll down
MAX_SCROLL_AMOUNT = -1     # can adjust direction/speed

# Number of scroll events (or use a while loop)
TOTAL_SCROLLS = 3000000

print("Starting auto scroller... Press Ctrl+C to stop.")

try:
    for i in range(TOTAL_SCROLLS):
        # Pick random values within the defined range
        scroll_amount = random.randint(MIN_SCROLL_AMOUNT, MAX_SCROLL_AMOUNT)
        interval = random.uniform(MIN_SCROLL_INTERVAL, MAX_SCROLL_INTERVAL)

        # Perform the scroll
        pyautogui.scroll(scroll_amount)
        print(f"[{i+1}] Scrolled: {scroll_amount} | Next in: {interval:.2f}s")

        # Wait before next scroll
        time.sleep(interval)

except KeyboardInterrupt:
    print("\nScrolling stopped by user.")