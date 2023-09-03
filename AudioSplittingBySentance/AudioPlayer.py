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
import Config
import logging
import json
import AudioPreprocessor

pygame.init()


class AudioPlayer:
    def __init__(self):
        self.waves_dir_path = None
        self.out_metadata_file_path = None
        self.in_text_file_path = None
        self.sound = None
        self.played_song_index = None
        self.audio_dict = {}

        self.logger = logging.getLogger("error_logger")
        self.logger.setLevel(logging.ERROR)
        file_handler = logging.FileHandler("Error.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def initUI(self):
        self.root = Tk()

        # Create a menu bar
        self.menubar = Menu(self.root)

        # Create a File menu and add it to the menu bar
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=lambda: self.open_config_file())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        # Configure the root window to display the menu bar
        self.root.config(menu=self.menubar)

        self.root.title("Audio Player")
        self.out_csv_file_path = self.out_metadata_file_path

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        self.font = tkFont.Font(family="helvetica", size=18)
        self.text_widget = Text(self.root, font=self.font, selectforeground='black')
        self.text_widget.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # scrolltext_widget = ttk.Scrollbar(root, orient=tk.VERTICAL)
        #
        # scrolltext_widget.pack(side=tk.RIGHT, fill=tk.Y)
        # scrolltext_widget.config(command=text_widget.yview)
        # text_widget.config(xscrollcommand=scrolltext_widget.set)

        # frame = Frame(root, height=height, width=width/2)
        # frame.pack(fill=BOTH, expand=True)

        self.listbox = Listbox(self.root, font=self.font)
        self.listbox.pack(padx=10, pady=10, side=LEFT, fill=BOTH, expand=True)

        # scrolllistbox = ttk.Scrollbar(root, orient=tk.VERTICAL)
        # scrolllistbox.pack(side=tk.RIGHT, fill=tk.X)
        # scrolllistbox.config(command=listbox.yview)
        # listbox.config(xscrollcommand=scrolllistbox.set)

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

        self.text_widget.bind("<B1-Motion>", lambda event: self.text_widget.tag_add(SEL, "sel.first", "sel.last"))
        self.text_widget.bind("<B1-Motion>", lambda event: self.text_widget.tag_config(SEL, background="yellow"))

        self.text_widget.bind("<ButtonRelease-1>", lambda event: self.save_pair())

        self.listbox.bind("<Double-Button-1>", self.play_audio)

        #self.scan_directory()

    def open_config_file(self):
        config = filedialog.askopenfilename(initialdir="/", title="Select config file",
                                            filetypes=(("json file", "*.json"), ("json file", "*.json")))
        print(config)
        with open(config, "r") as file:
            data = json.load(file)
        print(data["AudioPlayer"])
        self.in_text_file_path = data["AudioPlayer"]["docx_file"]
        self.out_metadata_file_path = data["AudioPlayer"]["metadata_file"]
        self.waves_dir_path = data["AudioPlayer"]["input_wav_dir"]

        if not os.path.exists(self.in_text_file_path):
            self.logger.error(f"{self.in_text_file_path} File not exist:")
            return
        text = TextUtilities.read_docx_file(self.in_text_file_path)
        self.text_widget.insert(END, text)

        # if not os.path.exists(out_metadata_file_path):
        #     self.logger.error(f"{out_metadata_file_path} File not exist:")
        #     return
        if not os.path.exists(self.waves_dir_path):
            self.logger.error(f"{self.waves_dir_path} Directory not exist:")
            print(f"{self.waves_dir_path} Directory not exist:")
            print(f"{self.waves_dir_path} Starting AudioPreprocessing")
            preproc = AudioPreprocessor.AudioPreprocessor(
                mp3_file_path=data["AudioPreproc"]["mp3_audio"],
                wav_file_path=data["AudioPreproc"]["wav_audio"],
                docx_file_path=data["AudioPreproc"]["docx_file"],
                metadata_file_path=data["AudioPreproc"]["metadata_file"],
                out_waves_dir=self.waves_dir_path)
            preproc.start()
        self.scan_directory()

    def scan_directory(self):
        files = os.listdir(self.waves_dir_path)
        files = sorted(files, key=lambda x: os.stat(os.path.join(self.waves_dir_path, x)).st_ctime)
        for file in files:
            if file.endswith(".mp3") or file.endswith(".wav"):
                filename = os.path.join(self.waves_dir_path, file)
                self.listbox.insert(END, file)
                self.audio_dict[file] = filename

    def import_files(self):
        filenames = filedialog.askopenfilenames(initialdir="/", title="Select audio files",
                                                filetypes=(("mp3 files", "*.mp3"), ("wav files", "*.wav")))
        for filename in filenames:
            name = os.path.basename(filename)
            self.listbox.insert(END, name)
            self.audio_dict[name] = filename

    def play_audio(self, event):
        self.stop_audio()
        index = self.listbox.curselection()[0]
        self.played_song_index = index
        item = self.listbox.get(index)
        name = item.split(" - ")[0]
        filename = self.audio_dict[name]
        self.sound = pygame.mixer.Sound(filename)
        self.sound.play()
        self.listbox.itemconfig(index, bg="green")

    def stop_audio(self):
        if self.sound:
            self.sound.stop()

    def remove_functionality(self):
        sel = self.listbox.curselection()
        for index in reversed(sel):
            self.listbox.delete(index)
            item = self.listbox.get(index)
            name = item.split(" - ")[0]
            del self.audio_dict[name]

    def save_pair(self):
        print(f"played_song_index: {self.played_song_index}")
        if self.played_song_index is not None:
            index = self.played_song_index
            self.played_song_index = None
            print(f"index: {index}")
            song = self.listbox.get(index)
            print(f"song: {song}")
            print(f"SEL_FIRST: {SEL_FIRST}")
            print(f"SEL_LAST: {SEL_LAST}")
            text = self.text_widget.get(SEL_FIRST, SEL_LAST)
            self.text_widget.tag_config("green", foreground="green")
            self.text_widget.tag_add("green", SEL_FIRST, SEL_LAST)
            print(f"text: {text}")
            with open(self.out_metadata_file_path, "a", newline="",
                      encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile, delimiter="|")
                writer.writerow([song, text])
        else:
            print("Please select an item in the listbox")

    def run(self):
        self.initUI()
        self.root.mainloop()


player = AudioPlayer()
player.run()
