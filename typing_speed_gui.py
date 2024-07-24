# importing all libraries
from tkinter import *
from timeit import default_timer as timer
import random

# creating window using gui
window = Tk()

# setting window title and background color
window.title("Typing Speed Test")
window.configure(bg='lightblue')

# the size of the window is defined
window.geometry("450x200")

x = 0

# defining the function for the test
def game():
    global x, start, words, word, entry, windows, results_label

    # loop for destroying the window
    # after one test
    if x == 0:
        window.destroy()
        x = x + 1

    # defining function for results of test
    def check_result():
        end = timer()
        time_taken = end - start
        typed_text = entry.get()

        # Calculating WPM
        word_count = len(typed_text.split())
        wpm = word_count / (time_taken / 60)

        # Calculating Accuracy
        original_text = words[word]
        typed_words = typed_text.split()
        original_words = original_text.split()
        correct_words = sum(1 for tw, ow in zip(typed_words, original_words) if tw == ow)
        accuracy = (correct_words / len(original_words)) * 100

        # Display results
        results_text = f"Time: {time_taken:.2f} seconds\nSpeed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        results_label.config(text=results_text)

    words = ['software', 'processing', 'database','cloud', 'programming', 'coding', 'algorithm', 'systems', 'python', 'hardware']

    # Give random words for testing the speed of user
    word = random.randint(0, (len(words) - 1))

    # start timer using timeit function
    start = timer()
    windows = Tk()
    windows.title("Typing Speed Test - In Progress")
    windows.configure(bg='thistle')
    windows.geometry("450x300")

    # use label method of tkinter for labeling in window
    x2 = Label(windows, text=words[word], font="times 20", bg='thistle')

    # place of labeling in window
    x2.place(x=150, y=10)
    x3 = Label(windows, text="Start Typing", font="times 20", bg='thistle')
    x3.place(x=10, y=50)

    entry = Entry(windows)
    entry.place(x=280, y=55)

    # buttons to submit output and check results
    b2 = Button(windows, text="Done", command=check_result, width=12, bg='bisque')
    b2.place(x=150, y=100)

    b3 = Button(windows, text="Try Again", command=game, width=12, bg='bisque')
    b3.place(x=250, y=100)

    results_label = Label(windows, text="", font="times 20", bg='thistle')
    results_label.place(x=150, y=150)

    windows.mainloop()

x1 = Label(window, text="Let's start playing..", font="times 20", bg='lightblue')
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg='bisque')
b1.place(x=150, y=100)

# calling window
window.mainloop()
