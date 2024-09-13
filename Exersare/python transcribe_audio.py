import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file into the recognizer
audio_file_path = "Fisierul_transformat_de_Py.wav"
with sr.AudioFile(audio_file_path) as source:
    audio_data = r.record(source)

# Perform the transcription
transcription = r.recognize_google(audio_data, language="ro-RO")

# Save the transcription to a text file
with open("transcription.txt", "w", encoding="utf-8") as f:
    f.write(transcription)

print("Transcription completed and saved to 'transcription.txt'")
