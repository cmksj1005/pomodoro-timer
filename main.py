import tkinter
import math

# Let's add motivation sentences

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    # If it's the 8th rep:
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # If it's the 1st/3rd/5th/7th rep:
    else:
        title_label.config(text="Study🔥", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_label.config(text=add_check(reps))


def add_check(reps):
    check_num = math.floor(reps / 2)
    check = ""
    for _ in range(check_num):
        check += "✔️"
    return check


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=300, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(150, 112, image=tomato_img)
timer_text = canvas.create_text(
    150, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

title_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN
)
title_label.grid(column=1, row=0)
check_label = tkinter.Label(text="", font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

start_button = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
reset_button = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

window.mainloop()
