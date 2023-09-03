import wave
import audioop
import pydub
import webrtcvad
import math

# define some constants
TARGET_DBFS = -26  # target volume level in dBFS
SAMPLE_RATE = 22050  # target sampling rate in Hz
SAMPLE_WIDTH = 2  # target bit depth in bytes
FRAME_DURATION = 30  # frame duration in ms
VAD_MODE = 3  # VAD aggressiveness mode (0-3)


# define a function to resample the audio data to match the new sampling rate and bit depth
def resample_audio(data_in, sampwidth_in, nchannels_in, framerate_in, sampwidth_out, framerate_out):
    # resample the original audio data using linear interpolation
    data_out = audioop.ratecv(data_in, sampwidth_in, nchannels_in, framerate_in, framerate_out, None)[0]
    # convert the bit depth of the resampled audio data using linear conversion
    data_out = audioop.lin2lin(data_out, sampwidth_in, sampwidth_out)
    # return the resampled audio data
    return data_out


# define a function to normalize the volume level of the audio data to match the target dBFS
def normalize_volume(data_in, sampwidth_in):
    # calculate the average volume level of the input audio data in dBFS
    avg_dbfs = 20 * math.log10(audioop.rms(data_in, sampwidth_in))
    # calculate the scaling factor to normalize the volume level to the target dBFS
    scale = math.pow(10.0, (TARGET_DBFS - avg_dbfs) / 20.0)
    # normalize the volume level of the input audio data by multiplying with the scaling factor
    data_out = audioop.mul(data_in, sampwidth_in, scale)
    # return the normalized audio data
    return data_out


# define a function to segment the audio data using WebRTC VAD
def segment_speech(data_in):
    # create a VAD object with the specified mode
    vad = webrtcvad.Vad(VAD_MODE)
    # calculate the frame size in bytes
    frame_size = int(SAMPLE_RATE * FRAME_DURATION / 1000) * SAMPLE_WIDTH
    # initialize an empty list for storing speech segments
    speech_segments = []
    # loop over the frames of the input audio data
    for i in range(0, len(data_in), frame_size):
        # get a frame of audio data
        frame = data_in[i:i + frame_size]
        # check if the frame contains speech or not using VAD
        is_speech = vad.is_speech(frame, SAMPLE_RATE)
        # if the frame contains speech, append it to the speech segments list
        if is_speech:
            speech_segments.append(frame)
    # join the speech segments into a single string
    data_out = b"".join(speech_segments)
    # return the segmented audio data
    return data_out


# open the original audio file in read mode
wav_in = wave.open("output/adamamutin_anahit_kirakosyan/wavs/segment_0.wav", "r")

# get the original parameters
nchannels, sampwidth, framerate, nframes, comptype, compname = wav_in.getparams()

# read the original audio data as a string
data_in = wav_in.readframes(nframes)

# close the original audio file
wav_in.close()

# create a new wave file in write mode
wav_out = wave.open("output/adamamutin_anahit_kirakosyan/wavs/segment_0_0.wav", "w")

# set the new parameters
wav_out.setnchannels(nchannels)
wav_out.setsampwidth(SAMPLE_WIDTH)
wav_out.setframerate(SAMPLE_RATE)
wav_out.setcomptype(comptype, compname)

# resample the original audio data to match the new sampling rate and bit depth
data_out = resample_audio(data_in, sampwidth, nchannels, framerate, SAMPLE_WIDTH, SAMPLE_RATE)

# normalize the volume level of the resampled audio data to match the target dBFS
data_out = normalize_volume(data_out, SAMPLE_WIDTH)

# segment the normalized audio data using WebRTC VAD
data_out = segment_speech(data_out)

# write the modified audio data to the new wave file
wav_out.writeframes(data_out)

# close the new wave file
wav_out.close()

# create an audio segment from the original audio file
audio_in = pydub.AudioSegment.from_file("output/adamamutin_anahit_kirakosyan/wavs/segment_0.wav")

# split the audio segment into two mono audio segments if it is stereo
if audio_in.channels == 2:
    audio_in = audio_in.split_to_mono()[0]

# create an audio segment from the new wave file
audio_out = pydub.AudioSegment.from_file("output/adamamutin_anahit_kirakosyan/wavs/segment_0_1.wav")

# get the original and modified transcriptions from the corresponding files
# with open("original.txt", "r") as f_in:
#     transcript_in = f_in.read()
# with open("modified.txt", "r") as f_out:
#     transcript_out = f_out.read()
#
# # print the original and modified transcriptions
# print("Original transcription:")
# print(transcript_in)
# print("Modified transcription:")
# print(transcript_out)
