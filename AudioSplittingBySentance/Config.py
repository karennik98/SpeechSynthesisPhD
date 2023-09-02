import os

docx_file_path = "input\\002.docx"

audio_file_path = 'input\\002.mp3'
wav_file_path = "input\\002.wav"

output_dir_path = 'output\\'
if not os.path.exists(output_dir_path):
    os.makedirs(output_dir_path)
    print("Created folder:", output_dir_path)
else:
    print(output_dir_path, "folder already exists.")

adamamutin_file_path_mp3 = "input\\adamamutin_anahit_kirakosyan\\001_cut.mp3"
adamamutin_file_path_wav = "input\\adamamutin_anahit_kirakosyan\\001_cut.wav"
adamamutin_docx_file_path = "input\\adamamutin_anahit_kirakosyan\\adamamutin.docx"
adamamutin_output_dir_path = 'output\\adamamutin_anahit_kirakosyan\\wavs\\'
if not os.path.exists(adamamutin_output_dir_path):
    os.makedirs(adamamutin_output_dir_path)
    print("Created folder:", adamamutin_output_dir_path)
else:
    print(adamamutin_output_dir_path, "folder already exists.")

adamamutin_output_csv_dir_path = 'output\\adamamutin_anahit_kirakosyan\\metadata.csv'
adamamutin_player_output_csv_file_path = 'output\\adamamutin_anahit_kirakosyan\\adamamutin_metadata.csv'


min_diff_threshold = 0.7
split_character=':'

# # Create a menu bar
# self.menubar = ttk.Menu(self.root)
#
# # Create a File menu and add it to the menu bar
# filemenu = ttk.Menu(self.menubar, tearoff=0)
# filemenu.add_command(label="New", command=lambda: self.show_message("New file"))
# filemenu.add_command(label="Open", command=lambda: self.show_message("Open file"))
# filemenu.add_command(label="Save", command=lambda: self.show_message("Save file"))
# filemenu.add_separator()
# filemenu.add_command(label="Exit", command=self.root.quit)
# self.menubar.add_cascade(label="File", menu=filemenu)
#
# # Create an Edit menu and add it to the menu bar
# editmenu = ttk.Menu(self.menubar, tearoff=0)
# editmenu.add_command(label="Cut", command=lambda: self.show_message("Cut text"))
# editmenu.add_command(label="Copy", command=lambda: self.show_message("Copy text"))
# editmenu.add_command(label="Paste", command=lambda: self.show_message("Paste text"))
# self.menubar.add_cascade(label="Edit", menu=editmenu)
#
# # Configure the root window to display the menu bar
# self.root.config(menu=self.menubar)