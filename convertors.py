from pypinyin import pinyin, Style


def character_to_pinyin(characters):
    """Gets a pinyin string from the characters."""
    results = list(''.join(x) for x in pinyin(characters, style=Style.TONE3))
    for i in range(0, len(results)):
        if "1" not in results[i] and "2" not in results[i] and "3" not in results[i] and "4" not in results[i]:
            results[i] = results[i] + "5"
        results[i] = results[i].replace("v", "uu")
    return results
