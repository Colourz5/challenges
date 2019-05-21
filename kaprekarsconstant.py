def KaprekarsConstant(num):
    steps = 0
    while True:
        num = "{0:04}".format(num)
        ascend = int("".join(sorted(num)))
        descend = int("".join(sorted((num), reverse=True)))
        num = descend - ascend
        steps += 1
        if num == 6174:
            return steps
