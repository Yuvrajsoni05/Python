n1 = int(input("Enter First Number : "))
n2 = int(input("Enter Second Number "))
n3 = input("how can i help You : ")

match n3:
    case "add":
        n4 = n1 + n2
        print(n4)
    case "sub":
        n4 = n1 - n2
        print(n4)
    case _:
        print("valid")