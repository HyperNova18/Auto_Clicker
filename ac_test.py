import time
import threading
import pyautogui
import keyboard

class AutoClicker:
    def __init__(self, interval=0.001):
        self.interval = interval
        self.running = False
        self.click_thread = None

    def start_clicking(self):
        self.running = True
        self.click_thread = threading.Thread(target=self.click_loop)
        self.click_thread.start()

    def stop_clicking(self):
        self.running = False

    def click_loop(self):
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

if __name__ == "__main__":
    auto_clicker = AutoClicker()
    print("AutoClicker started. Press F6 to toggle.")
    
    def toggle_auto_clicker():
        if auto_clicker.running:
            auto_clicker.stop_clicking()
            print("AutoClicker stopped.")
        else:
            auto_clicker.start_clicking()
            print("AutoClicker started.")
    
    keyboard.add_hotkey('F6', toggle_auto_clicker)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        keyboard.remove_hotkey('F6')
        print("Exiting.")
