def LongestWord(sen):
    punctuation = str.maketrans("!?.,'\\\"/[](){}+-*=-_<>|%#@^&~`", 30*" ")
    sentence = sen.split(" ")
    longest = ""
    for word in sentence:
        word = word.translate(punctuation)
        word = word.replace(" ", "")
        if len(word) > len(longest):
            longest = word
    return longest
    