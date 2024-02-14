import pyautogui
import time
import tkinter as tk

class ClickApp:
    def __init__(self, master):
        self.master = master
        master.title("Click App")
        master.geometry("250x100")

        self.label = tk.Label(master, text="Click the button to simulate 3 clicks")
        self.label.pack(pady=3)

        self.click_button = tk.Button(master, text="Simulate Clicks", command=self.simulate_multiple_clicks)
        self.click_button.pack()

    def simulate_multiple_clicks(self):
        original_position = pyautogui.position()
        click_position = pyautogui.position()

        for _ in range(5):
            pyautogui.click(click_position)
            time.sleep(0.1)

        pyautogui.moveTo(original_position)

if __name__ == "__main__":
    root = tk.Tk()
    app = ClickApp(root)
    root.mainloop()
