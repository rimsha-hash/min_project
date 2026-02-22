def number():
    while True:
        try:
            num=int(input("enter number: "))
            break
        except ValueError:
            print(" Invalid number:please inter a valid number ")
number(5)