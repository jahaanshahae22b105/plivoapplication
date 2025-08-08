import speech_recognition as sr

def transcribe_offline(audio_file):
    audio_file.seek(0)
    recognizer = sr.Recognizer()
    try:
        # speech_recognition.AudioFile can take a file-like object
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
        transcript = recognizer.recognize_sphinx(audio_data)
    except Exception as e:
        transcript = f"Transcription error: {e}"
    return {'text': transcript}
