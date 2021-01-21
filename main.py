from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import pygame

music = ""
pygame.mixer.init()
looped = 0
paused = False


def play():
    if not music == "":
        stats.configure(text="Playing", fg="green")
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
    else:
        showinfo(title="Error", message="Please select which music to play")


def upload():
    global music
    file = filedialog.askopenfilename()
    if not file == "":
        music = file
        file_name.configure(text=music)
    else:
        pass


def loop():
    global looped
    if looped == 0:
        looped = 1
    else:
        looped = 0


def stop():
    stats.configure(fg="red", text="Not Playing")
    pygame.mixer.music.stop()


def pause():
    global paused
    if not paused:
        paused = True
        stats.configure(text="Paused", fg="orange")
        pygame.mixer.music.pause()
    else:
        paused = False
        stats.configure(text="Playing", fg="green")
        pygame.mixer.music.unpause()


def select():
    showinfo(title="Coming in v 2021.1!", message="Library coming in v 2021.1!")


window = Tk()
window.title('Music World')
window.minsize(500, 400)
window.maxsize(500, 400)

play_btn = PhotoImage(file='play.png')
pause_btn = PhotoImage(file="pause.png")
stop_btn = PhotoImage(file="stop.png")

play_button = Button(window, image=play_btn, command=play)
play_button.pack()

pause_button = Button(window, image=pause_btn, command=pause)
pause_button.pack()

stop_button = Button(window, image=stop_btn, command=stop)
stop_button.pack()

version = Label(text="version = 2021.0")
version.pack(side=BOTTOM)

stats = Label(font=("Helvetica", 10), fg="red", text="Not Playing")
stats.pack(side=BOTTOM)

file_name = Label(window, font=("Helvetica", 10), text="No File Selected")
file_name.pack(side=BOTTOM)

menu = Menu(window)
music_menu = Menu(menu, tearoff=0)
menu.add_cascade(menu=music_menu, label="Music")
music_menu.add_command(label="Select", command=select)
music_menu.add_command(label="Upload", command=upload)
music_menu.add_command(label="Looped", command=loop)

window.configure(menu=menu)
window.mainloop()
