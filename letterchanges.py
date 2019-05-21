def LetterChanges(str):
    str = list(str)
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = lower.upper()
    lower_shift = lower[1:] + lower[:1]
    upper_shift = upper[1:] + upper[:1]
    lower = list(lower)
    upper = list(upper)
    vowels = list("aeiou")
    for place, character in enumerate(str):
        if character in lower:
            index = lower.index(character)
            str[place] = lower_shift[index]
        elif character in upper:
            index = upper.index(character)
            str[place] = upper_shift[index]
    for place, character in enumerate(str):
        if character in vowels:
            str[place] = character.upper()
    str = "".join(str)
    return str
