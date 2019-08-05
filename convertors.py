from pypinyin import pinyin, Style


def character_to_pinyin(characters):
    """Gets a pinyin string from the characters."""
    return ''.join(''.join(x) for x in pinyin(characters, style=Style.TONE2))
