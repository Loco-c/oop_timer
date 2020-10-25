import tkinter as tk
import time


class TimeClock:
    def __init__(self):
        self.window = window = tk.Tk()
        self.t_display = tk.Label(window, text="", font=("Aria", 48), fg="green", bg="black")
        self.t_display.pack()
        self.update()
        self.window.mainloop()
        # Displaying window sizes as set before
        window.title("timer")
        window.geometry("200x100")

    def update(self):
        currentclock = time.strftime("%H:%M:%S")
        self.t_display.configure(text=currentclock)
        self.window.after(1000, self.update)


timeclock = TimeClock()
