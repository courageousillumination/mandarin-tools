import requests
from os import path
from pydub import AudioSegment

BASE_URL = "https://www.mdbg.net/chinese/rsc/audio/voice_pinyin_pz/"


def download_sound(word, directory):
    file_name = f"{directory}{word}.mp3"
    if path.exists(file_name):
        return file_name

    print(f"Downloading audio for {word}")
    url = f"{BASE_URL}{word}.mp3"
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_name, 'wb') as f:
            f.write(response.content)
        return file_name
    except requests.exceptions.HTTPError:
        print(f"Could not download file for {word}")
        return ""


def download_samples(words, directory):
    file_name = f"{directory}{''.join(words)}.mp3"
    if path.exists(file_name):
        return file_name

    # Download each sound
    files = [download_sound(word, directory) for word in words]

    sound = AudioSegment.from_mp3(files[0])
    for i in range(1, len(files)):
        sound += AudioSegment.from_mp3(files[i])

    sound.export(file_name, format="mp3")
    return file_name
