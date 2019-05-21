def SimpleSymbols(str):
    for index, character in enumerate(list(str)):
        if character.isalpha():
            if index == 0:
                return "false"
            if index == len(str) - 1:
                return "false"
            if str[index - 1] != "+" or str[index + 1] != "+":
                return "false"
    return "true"
