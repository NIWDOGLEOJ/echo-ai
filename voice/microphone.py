from voice.speech_to_text import listen


def listen_continuous():
    while True:
        text = listen()

        if text:
            print("Heard:", text)
            return text