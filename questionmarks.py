import sys


def QuestionsMarks(str):
    digits = list("0123456789")
    num_index = []
    # keep list of where in the string there is a digit
    for i in range(len(str)):
        if str[i] in digits:
            num_index.append(i)
    # list of tuples of pairs of indexes which has digits which sum to 10
    nums_add_10 = []
    for first_index in range(len(num_index) - 1):
        num1 = int(str[num_index[first_index]])
        num2 = int(str[num_index[first_index + 1]])
        if num1 + num2 == 10:
            nums_add_10.append((num_index[first_index],
                                num_index[first_index + 1]))
    # if there are no pairs of digits which add to 10 return false
    if len(nums_add_10) == 0:
        return False
    # go through all the pairs and check between them if there are exactly 3 ?
    for i in range(len(nums_add_10)):
        count = 0
        for j in range(nums_add_10[i][0] + 1, nums_add_10[i][1]):
            if str[j] == "?":
                count += 1
        if count != 3:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(QuestionsMarks(sys.argv[1]))
    else:
        argument = input("Enter string to check here: ")
        print(QuestionsMarks(argument))
        input("Press enter to exit: ")
