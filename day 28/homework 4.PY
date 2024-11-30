try:    
    score = float(input("შეიყვანეთ სტუდენტის ქულა (0-დან 100-მდე): "))

    if 90 <= score <= 100:
        print("შეფასება: A")
    elif 80 <= score < 90:
        print("შეფასება: B")
    elif 70 <= score < 80:
        print("შეფასება: C")
    elif 60 <= score < 70:
        print("შეფასება: D")
    elif 0 <= score < 60:
        print("შეფასება: F")
    else:
        print("შეიყვანეთ ვალიდური ქულა 0-დან 100-მდე.")
except ValueError:
    print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")
