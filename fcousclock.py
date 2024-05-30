import tkinter as tk  
from tkinter import messagebox  
from time import sleep  
  
class PomodoroTimer(tk.Frame):  
    def __init__(self, root, interval=25*60):  # 默认25分钟  
        super().__init__(root)  
        self.init_ui(interval)  
  
    def init_ui(self, interval):  
        self.master.title("Pomodoro Timer")  
  
        self.label = tk.Label(self, text="25:00", font=("Helvetica", 48))  
        self.label.pack(expand=1)  
  
        self.interval = interval  
        self.remaining = interval  
  
        self.update_timer()  
  
        self.start_button = tk.Button(self, text="Start", command=self.start_timer)  
        self.start_button.pack(side=tk.LEFT, padx=20, pady=20)  
  
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_timer)  
        self.reset_button.pack(side=tk.RIGHT, padx=20, pady=20)  
  
        self.pack(fill=tk.BOTH, expand=1)  
  
    def update_timer(self):  
        minutes, seconds = divmod(self.remaining, 60)  
        timer_str = "{:02d}:{:02d}".format(minutes, seconds)  
        self.label.config(text=timer_str)  
  
        if self.remaining > 0:  
            self.remaining -= 1  
            self.after(1000, self.update_timer)  # 每秒更新一次  
        else:  
            self.start_button.config(text="Restart", command=self.restart_timer)  
            messagebox.showinfo("Time's Up!", "Pomodoro session is over!")  
  
    def start_timer(self):  
        self.update_timer()  # 开始时立即更新一次  
  
    def reset_timer(self):  
        self.remaining = self.interval  
        self.update_timer()  # 重置后更新显示  
  
    def restart_timer(self):  
        self.remaining = self.interval  
        self.start_timer()  
  
def main():  
    root = tk.Tk()  
    root.geometry("300x200")  
    app = PomodoroTimer(root)  
    app.mainloop()  
  
if __name__ == '__main__':  
    main()
