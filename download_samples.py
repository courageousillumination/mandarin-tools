import requests

BASE_URL = "https://www.mdbg.net/chinese/rsc/audio/voice_pinyin_pz/"
DATA_DIRECTORY = "data/"


def download_samples(words):
    for word in words:
        url = f"{BASE_URL}{word}.mp3"
        response = requests.get(url)
        with open(f"{DATA_DIRECTORY}{word}.mp3", 'wb') as f:
            f.write(response.content)
