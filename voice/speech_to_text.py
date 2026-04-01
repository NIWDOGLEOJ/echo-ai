import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()


def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text.lower()

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""