# Import Tkinter, Pygame, filedialog, os, and csv
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pygame
from tkinter import filedialog
import os
import csv
import TextUtilities

pygame.init()

root = Tk()
root.title("Audio Player")

style = ttk.Style()
# Map the background color of the listbox widget to green when selected
style.map("Listbox", background=[("selected", "green")])

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

font = tkFont.Font(family="helvetica", size=18)
text_widget = Text(root, font=font, selectforeground='black')
text_widget.pack(padx=10, pady=10, fill=BOTH, expand=True)

# scrolltext_widget = ttk.Scrollbar(root, orient=tk.VERTICAL)
#
# scrolltext_widget.pack(side=tk.RIGHT, fill=tk.Y)
# scrolltext_widget.config(command=text_widget.yview)
# text_widget.config(xscrollcommand=scrolltext_widget.set)

text = TextUtilities.read_docx_file('input/adamamutin_anahit_kirakosyan/adamamutin.docx')
text_widget.insert(END, text)

# frame = Frame(root, height=height, width=width/2)
# frame.pack(fill=BOTH, expand=True)

listbox = Listbox(root, font=font)
listbox.pack(padx=10, pady=10, side=LEFT, fill=BOTH, expand=True)

# scrolllistbox = ttk.Scrollbar(root, orient=tk.VERTICAL)
# scrolllistbox.pack(side=tk.RIGHT, fill=tk.X)
# scrolllistbox.config(command=listbox.yview)
# listbox.config(xscrollcommand=scrolllistbox.set)

sound = None
played_song_index = None
audio_dict = {}
text_dict = {}

with open("output/adamamutin_anahit_kirakosyan/metadata.csv", "r", newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter="|")
    for row in reader:
        name = row[0]
        text = row[1]
        text_dict[name] = text

dir_path = "C:\\Users\\karenn\\PhD\\SpeechSynthesisPhD\\AudioSplittingBySentance\\output\\adamamutin_anahit_kirakosyan\\wavs"

def scan_directory():
    files = os.listdir(dir_path)
    files = sorted(files, key=lambda x: os.stat(os.path.join(dir_path, x)).st_ctime)
    for file in files:
        if file.endswith(".mp3") or file.endswith(".wav"):
            filename = os.path.join(dir_path, file)
            if file in text_dict:
                listbox.insert(END, file)
                audio_dict[file] = filename

scan_directory()


def import_files():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select audio files",
                                            filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav")))
    for filename in filenames:
        name = os.path.basename(filename)
        if name in text_dict:
            listbox.insert(END, name)
            audio_dict[name] = filename

def play_audio(event):
    stop_audio()
    global played_song_index
    index = listbox.curselection()[0]
    played_song_index = index
    item = listbox.get(index)
    name = item.split(" - ")[0]
    filename = audio_dict[name]
    global sound
    sound = pygame.mixer.Sound(filename)
    sound.play()
    listbox.itemconfig(index, bg="green")

def stop_audio():
    global sound
    if sound:
        sound.stop()

def remove_functionality():
    sel = listbox.curselection()
    for index in reversed(sel):
        listbox.delete(index)
        item = listbox.get(index)
        name = item.split(" - ")[0]
        del audio_dict[name]

def save_pair():
    global played_song_index
    print(f"played_song_index: {played_song_index}")
    if played_song_index is not None:
        index = played_song_index
        played_song_index = None
        print(f"index: {index}")
        song = listbox.get(index)
        print(f"song: {song}")
        print(f"SEL_FIRST: {SEL_FIRST}")
        print(f"SEL_LAST: {SEL_LAST}")
        text = text_widget.get(SEL_FIRST, SEL_LAST)
        text_widget.tag_config("green", foreground="green")
        text_widget.tag_add("green", SEL_FIRST, SEL_LAST)
        print(f"text: {text}")
        with open("output/adamamutin_anahit_kirakosyan/pairs.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter="|")
            writer.writerow([song, text])
    else:
        print("Please select an item in the listbox")


text_widget.bind("<B1-Motion>", lambda event: text_widget.tag_add(SEL, "sel.first", "sel.last"))
text_widget.bind("<B1-Motion>", lambda event: text_widget.tag_config(SEL, background="yellow"))

text_widget.bind("<ButtonRelease-1>", lambda event: save_pair())

listbox.bind("<Double-Button-1>", play_audio)

# import_button = Button(frame, text="Import", command=import_files)
# import_button.pack(side=TOP)
#
# play_button = Button(frame, text="Play")
# play_button.pack(side=TOP)
# # Bind button to play_audio function with mouse click event
# play_button.bind("<Button-1>", play_audio)
#
# stop_button = Button(frame, text="Stop", command=stop_audio)
# stop_button.pack(side=TOP)
#
# remove_button = Button(frame, text="Remove", command=remove_functionality)
# remove_button.pack(side=TOP)

root.mainloop()
