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

MODEL = genanki.Model(1362345001,
                      'Mandarin Character + Pinyin + English',
                      fields=[
                          {'name': 'Character'},
                          {'name': 'Pinyin'},
                          {'name': 'PronunciationMedia'},
                          {'name': 'English'}
                      ],
                      css=CSS,
                      templates=[
                          {
                              'name': 'Character to English/Pinyin',
                              'qfmt': '{{Character}}',
                              'afmt': '{{FrontSide}}<hr id="answer">{{Pinyin}} ({{English}})<br>{{PronunciationMedia}}',
                          },
                          {
                              'name': 'English to Character/Pinyin',
                              'qfmt': '{{English}}',
                              'afmt': '{{FrontSide}}<hr id="answer">{{Character}} ({{Pinyin}})<br>{{PronunciationMedia}}',
                          },
                          {
                              'name': 'Pinyin to Character/English',
                              'qfmt': '{{Pinyin}}<br>{{PronunciationMedia}}',
                              'afmt': '{{FrontSide}}<hr id="answer">{{Character}} ({{English}})',
                          },
                      ])


def create_note(vocab_triad):
    return genanki.Note(
        model=MODEL,
        fields=[vocab_triad.character, vocab_triad.pinyin,
                f"[sound:{vocab_triad.audio.split('/')[-1]}]", vocab_triad.english]
    )


def create_deck(vocab):
    deck = genanki.Deck(
        1832707768,
        'Mandarin (Characters, Pinyin, English)')
    for v in vocab:
        deck.add_note(create_note(v))
    package = genanki.Package(deck)
    package.media_files = [v.audio for v in vocab]
    package.write_to_file('mandarin.apkg')
