def FirstReverse(str):
    reverse = str[::-1]
    return reverse


if __name__ == "__main__":
    ask = input("Enter a string: ")
    print(FirstReverse(ask))