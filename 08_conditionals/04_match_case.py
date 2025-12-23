a = int(input("Enter a lucky number: "))

match a:
    case 122:
        print("the value is 122")
    case 34:
        print("the value is 3")
    case 6:
        print("the value is 6")
    case _:
        print("better luck next time")
    