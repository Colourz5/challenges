import sys


def repetition(word):
    word_list = list(word)
    repetition = []
    for index_1, character_1 in enumerate(word_list):
        index = "0"
        for index_2, character_2 in enumerate(word_list[(index_1 + 1):]):
            if character_1 == character_2:
                index = "+{}".format(index_2 + 1)
                break
        repetition.append(index)
    return repetition


def check_isomorph(isomorph_1, isomorph_2):
    repetition_1 = repetition(isomorph_1)
    repetition_2 = repetition(isomorph_2)
    if repetition_1 == repetition_2:
        return True, repetition_1
    return False, repetition_1


def output(isomorph_1, isomorph_2):
    string = ""
    if len(isomorph_1) != len(isomorph_2):
        string = "{}, {} have different lengths".format(isomorph_1, isomorph_2)
        return string
    isomorph_flag, pattern = check_isomorph(isomorph_1, isomorph_2)
    if isomorph_flag:
        pattern = " ".join(pattern)
        string = "{}, {} are isomorphs with repetition pattern {}".format(isomorph_1, isomorph_2, pattern)
    else:
        string = "{}, {} are not isomorphs".format(isomorph_1, isomorph_2)
    return string


if __name__ == "__main__":
    try:
        paircount = int(input())
        if paircount > 20:
            raise ValueError
    except ValueError:
        print("Error: Invalid input")
        sys.exit()
    pair_list = []
    for i in range(paircount):
        pairs = input()
        pairs = pairs.split()
        if len(pairs) != 2:
            print("Error: Input was not in pairs!")
            sys.exit()
        pair_list.append(pairs)
    print()
    for pair in pair_list:
        word_1 = pair[0]
        word_2 = pair[1]
        print(output(word_1, word_2))
