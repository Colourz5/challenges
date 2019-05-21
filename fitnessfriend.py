def take_input():
    motive_start = input()
    motivation, start_target = motive_start.split()
    motivation = int(motivation)
    start_target = int(start_target)
    steps = []
    while True:
        step_count = int(input())
        if step_count == -1:
            break
        steps.append(step_count)
    return (motivation, start_target, steps)


def process(motivation, start_target, steps):
    days = len(steps)
    mean = round(sum(steps) / len(steps))
    target = start_target
    k_factor = motivation / 100
    reached = 0
    targets = [str(target)]
    for day in range(days):
        if steps[day] >= target:
            target = target + (k_factor ** 2) * (steps[day] - target)
            reached += 1
        else:
            target = target + ((1 - k_factor) ** 2) * (steps[day] - target)
        target = int(target)
        targets.append(str(target))
    reached = round(reached / days * 100)
    return (motivation, days, mean, reached, targets)


if __name__ == "__main__":
    motivation, start_target, steps = take_input()
    motivation, days, mean, reached, targets = process(motivation,
                                                       start_target,
                                                       steps)
    targets_display = " ".join(targets)
    display = "Motivation: {}, days {}, mean steps {}, ".format(motivation,
                                                                days,
                                                                mean)
    display += "goal reached {}%. Final target {}".format(reached, targets[-1])
    print(targets_display)
    print(display)
