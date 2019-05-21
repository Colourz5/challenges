import sys


def rats(num):
    num_reverse = int(num[::-1])
    total = int(num) + num_reverse
    num_sorted = "".join(sorted(str(total)))
    num_sorted = num_sorted.lstrip("0")
    return num_sorted


<<<<<<< HEAD
def periodfinder(startnum):
    count = 0
    visited = []
    num = str(startnum)
    while True:
        num = str(num)
        count += 1
        num = int(rats(num))
        if num in visited:
            break
        visited.append(num)
        if num > 10**12:
            return None
    start = visited.index(num)
    period = count - start - 1
    cycle = []
    for element in range(period):
        cycle.append(visited[start + element])
    cycle = sorted(cycle)
    return [period, start, cycle]

=======
def ratsspecial(num):
    num_reverse = int(num[::-1])
    total = int(num) + num_reverse
    num_sorted = "".join(sorted(str(total)))
    print("{} + {} = {}, sorted = {}".format(num,
                                             num_reverse,
                                             total,
                                             num_sorted))
    num_sorted = num_sorted.lstrip("0")
    return num_sorted


def periodfinder(startnum):
    count = 0
    visited = []
    num = str(startnum)
    while True:
        num = str(num)
        count += 1
        num = int(rats(num))
        if num in visited:
            break
        visited.append(num)
        if num > 10**12:
            return None
    start = visited.index(num)
    period = count - start - 1
    cycle = []
    for element in range(period):
        cycle.append(visited[start + element])
    cycle = sorted(cycle)
    return [period, start, cycle]

>>>>>>> ee3a0e14b0b76a6bfac7ef707116c45be79bf9c1

for number in range(1, 10000):
    result = periodfinder(number)
    if result is None:
        continue
    else:
        period, start, cycle = result
        cycle = " ".join(str(x) for x in cycle)
        print("Period: {}, occurs {} times, cycle: {}".format(period,
                                                              start,
                                                              cycle))
