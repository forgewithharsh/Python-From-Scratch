import time
import os

while True:
    os.system("""
    osascript -e 'display notification "You need to drink some water" with title "Hydration Reminder"'
    """)
    time.sleep(1800)