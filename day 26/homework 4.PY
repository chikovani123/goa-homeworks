answer = 42  

while True:
    user_input = int(input("guess th number: "))
    if user_input == answer:
        print("it right!")
        break
    else:
        print("it's worong")
