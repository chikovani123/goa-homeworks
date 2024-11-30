try:
    number = int(input("შეიყვანეთ რიცხვი: "))

    if number % 2 == 0:
        print(f"{number} არის ლუწი რიცხვი.")
    else:
        print(f"{number} არის კენტი რიცხვი.")
except ValueError:
    print("გთხოვთ, შეიყვანოთ ვალიდური მთელი რიცხვი.")
