def LetterCapitalize(str):
    words = str.split()
    for index, word in enumerate(words):
        words[index] = list(word)
        word = words[index]
        if word[0].isalpha():
            word[0] = word[0].upper()
        words[index] = "".join(word)
    result = " ".join(words)
    return result
