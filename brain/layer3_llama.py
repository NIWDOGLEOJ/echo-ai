# Layer 3 — Reasoning fallback

import requests

URL = "http://192.168.29.10:1234/v1/chat/completions"


def reason(command: str):

    prompt = f"""
You are a command parser.

Convert user sentence into simple command.

Examples:

"can you open safari" -> open safari
"please open music" -> open music
"i want calculator" -> open calculator
"launch chrome" -> open chrome
"quit safari" -> close safari

Only output the command.
Do not explain.

User: {command}
"""

    try:
        response = requests.post(
            URL,
            json={
                "model": "local-model",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0
            }
        )

        text = response.json()["choices"][0]["message"]["content"]
        return text.strip().lower()

    except:
        return None