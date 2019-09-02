from os import path
import csv

from convertors import character_to_pinyin
from download_samples import download_samples
from export_anki import create_deck


class VocabWord(object):
    def __init__(self, english, pinyin, hanzi):
        self.english = english
        self.pinyin = pinyin
        self.hanzi = hanzi

    def get_audio_file(self):
        pinyin2 = character_to_pinyin(self.hanzi)
        return download_samples(pinyin2, "data/")


def clean_vocab_list(vocab_list):
    """Removes any duplicates (based on hanzi) and cleans up vocab."""
    cleaned = []
    hanzi = []
    for word in vocab_list:
        if word.hanzi in hanzi:
            print(f"Removing duplicate word {word.hanzi}")
            continue
        word.english = word.english.lower()
        cleaned.append(word)
        hanzi.append(word.hanzi)
    print(f"Finished cleaning {len(cleaned)} words")
    return cleaned


def save_to_csv(vocab_list, fileName):
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, ["English", "Pinyin", "Hanzi"])
        writer.writeheader()
        for word in vocab_list:
            writer.writerow({
                'English': word.english,
                "Pinyin": word.pinyin,
                "Hanzi": word.hanzi
            })


def load_vocab_database_from_csv(fileName):
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile, quotechar="\"")
        return [
            VocabWord(x['English'], x['Pinyin'], x['Hanzi']) for x in reader
        ]