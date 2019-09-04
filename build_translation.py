from translate import translator


def translate_english(val):
    """Use english as the base."""
    characters = translator('en', 'zh', val)[0]
    if len(characters) == 1:
        print(characters[0][0])


def translate_character(val):
    """Use the character as a base."""
    results = translator('zh', 'en', val)
    print(results)


def build_translation(val):
    # translate_english(val)
    translate_character(val)
