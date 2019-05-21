def TimeConvert(num):
    hours = num // 60
    minutes = num % 60
    new_time = "{}:{}".format(hours, minutes)
    return new_time
