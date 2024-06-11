def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def main():
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    print(a, "+", b, "=", add(int(a), int(b)))
    print(a, "-", b, "=", subtract(int(a), int(b)))


if __name__ == "__main__":
    main()
