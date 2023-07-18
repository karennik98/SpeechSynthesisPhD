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


min_diff_threshold = 0.7
split_character=':'
