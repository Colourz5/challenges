import sys


def VowelSquare(strArr):
    vowels = list("aeiou")
    for i in range(len(strArr) - 1):
        for j in range(len(strArr[i]) - 1):
            if strArr[i][j] in vowels:
                vowel_tright = strArr[i][j+1] in vowels
                vowel_bleft = strArr[i+1][j] in vowels
                vowel_bright = strArr[i+1][j+1] in vowels
                if vowel_bleft and vowel_bright and vowel_tright:
                    return "{}-{}".format(i, j)
    return "not found"


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(eval(sys.argv[1]))
        # ["gg", "ff"]

# # keep this function call here
# print VowelSquare(raw_input())
