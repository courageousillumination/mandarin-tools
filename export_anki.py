import genanki

CSS = """
.card {
    font-family: arial;
    font-size: 40px;
    text-align: center;
    color: black;
    background-color: white;
}
"""

TEMPLATES = [
    {
        'name': 'Character to Pinyin/English',
        'qfmt': '{{Character}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}} ({{English}})<br>{{PronunciationMedia}}',
    },
    {
        'name': 'English to Pinyin/Character',
        'qfmt': '{{English}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}} ({{Character}})<br>{{PronunciationMedia}}',
    },
    {
        'name': 'Pinyin/Character to English',
        'qfmt': '{{Pinyin}} ({{Character}})<br>{{PronunciationMedia}}',
        'afmt': '{{FrontSide}}<hr id="answer">{{English}}',
    },
]

FIELDS = [
    {'name': 'Character'},
    {'name': 'Pinyin'},
    {'name': 'PronunciationMedia'},
    {'name': 'English'},
    {'name': 'foo'}
]

MEANING_MODEL = genanki.Model(1619790000,
                              'Mandarin (English <-> Pinyin/Character)',
                              fields=FIELDS,
                              css=CSS,
                              templates=[TEMPLATES[1], TEMPLATES[2]])
CHARACTER_MODEL = genanki.Model(1207263220,
                                'Mandarin (Character -> Pinyin/English)',
                                fields=FIELDS,
                                css=CSS,
                                templates=[TEMPLATES[0]])


def create_note(vocab_triad, model, model_number):
    return genanki.Note(
        model=model,
        fields=[vocab_triad.character, vocab_triad.pinyin,
                f"[sound:{vocab_triad.audio.split('/')[-1]}]", vocab_triad.english, f"{model_number}"]
    )


def create_deck(vocab):
    deck1 = genanki.Deck(1853682858, 'Mandarin (Meaning)')
    deck2 = genanki.Deck(1797317159, 'Mandarin (Characters)')
    for v in vocab:
        deck1.add_note(create_note(v, MEANING_MODEL, 1619790000))
        deck2.add_note(create_note(v, CHARACTER_MODEL, 1207263220))
    package = genanki.Package([deck1, deck2])
    package.media_files = [v.audio for v in vocab]
    package.write_to_file('mandarin.apkg')
