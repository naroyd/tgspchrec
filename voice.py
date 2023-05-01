import speech_recognition as sr
import moviepy.editor as mp
import os
from pydub import AudioSegment

def convert(file):
    ecp=os.path.splitext(os.path.basename(file))[1]
    name=fr'Temp/Voice/Voice/{os.path.splitext(os.path.basename(file))[0]}.wav'
    try:
        if ecp==".mp4":
            mp.VideoFileClip(file).audio.write_audiofile(name)
        elif ecp==".mp3":
            AudioSegment.from_mp3(file).export(name, format="wav")
        elif ecp==".ogg":
            AudioSegment.from_ogg(file).export(name, format="wav")
    except:
        return -1
    return name

def recognition(file):
    if os.path.splitext(os.path.basename(file))[1]!=".wav": n_file = convert(file)
    else: n_file = file
    if n_file!=-1:
        try:
            r = sr.Recognizer()
            r.pause_threshold = 1
            with sr.AudioFile(n_file) as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
        except: text = "I can't recognise the voice"
    else: text="Invalid file format"
    return [text, file, n_file]

