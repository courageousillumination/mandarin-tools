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

LINKS = """
Links: 
<a href="https://hanzicraft.com/character/{{Character}}">HanziCraft</a>
<a href="https://www.mdbg.net/chinese/dictionary?page=worddict&wdrst=0&wdqb={{Character}}">MDBG</a>
"""
TEMPLATES = [
    {
        'name':
        'Mandarin (Write)',
        'qfmt':
        '{{English}}',
        'afmt':
        '{{FrontSide}}<hr id="answer">{{Character}} ({{Pinyin}})<br>{{PronunciationMedia}}'
        + LINKS,
    },
    {
        'name':
        'Mandarin (Read)',
        'qfmt':
        '{{Character}}',
        'afmt':
        '{{FrontSide}}<hr id="answer">{{English}} ({{Pinyin}})<br>{{PronunciationMedia}}'
        + LINKS,
    },
    {
        'name':
        'Mandarin (Listen)',
        'qfmt':
        '{{PronunciationMedia}}',
        'afmt':
        '{{FrontSide}}<hr id="answer">{{English}} {{Pinyin}} ({{Character}})' +
        LINKS,
    },
    {
        'name':
        'Mandarin (Speak)',
        'qfmt':
        '{{English}}',
        'afmt':
        '{{FrontSide}}<hr id="answer">{{Pinyin}} ({{Character}})<br>{{PronunciationMedia}}'
        + LINKS,
    },
]

FIELDS = [
    {
        'name': 'Character'
    },
    {
        'name': 'Pinyin'
    },
    {
        'name': 'PronunciationMedia'
    },
    {
        'name': 'English'
    },
]

MODEL = genanki.Model(1619790001,
                      'Mandarin (Read, Write, Speak, Listen)',
                      fields=FIELDS,
                      css=CSS,
                      templates=TEMPLATES)


def create_note(vocab_word):
    return genanki.Note(
        model=MODEL,
        fields=[
            vocab_word.hanzi, vocab_word.pinyin,
            f"[sound:{vocab_word.get_audio_file().split('/')[-1]}]",
            vocab_word.english
        ])


def create_deck(vocab):
    deck = genanki.Deck(1853682859, 'Mandarin (Read, Write, Speak, Listen)')
    [deck.add_note(create_note(v)) for v in vocab]
    package = genanki.Package(deck)
    package.media_files = [v.get_audio_file() for v in vocab]
    package.write_to_file('mandarin.apkg')
