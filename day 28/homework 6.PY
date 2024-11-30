import random

random_number = random.randint(1, 10)

print("მე დავაგენერირე რიცხვი 1-დან 10-მდე. სცადე გამოიცნო!")

while True:
    try:
        guess = int(input("შეიყვანეთ თქვენი ვარაუდი: "))
        
        if guess == random_number:
            print("გილოცავთ! სწორად გამოიცანით!")
            break
        elif guess < random_number:
            print("ჩემი რიცხვი უფრო მაღალია. სცადეთ კიდევ.")
        else:
            print("ჩემი რიცხვი უფრო დაბალია. სცადეთ კიდევ.")
    except ValueError:
        print("გთხოვთ, შეიყვანეთ ვალიდური რიცხვი")
