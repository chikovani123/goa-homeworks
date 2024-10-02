#homework 1
user_input = input("please enter any number you want: ")
number = float(user_input) 
result = number == 10
print(result)

#homework 2
user_input = input("please enter any number you want: ")
number = int(user_input) 
result = number % 2 == 0 
print(result)

#homework 3
user_input = input("please enter any number you want: ")

number = float(user_input)  
result = 50 <= number <= 100
print(result)

#homework 4
# მომხმარებლისგან სამი რიცხვის შეყვანა
user_input1 = input("please enter any number you want: ")
user_input2 = input("please enter any number you want: ")
user_input3 = input("please enter any number you want: ")

number1 = float(user_input1) 
number2 = float(user_input2)
number3 = float(user_input3) 

result = number1 != number2 and number1 != number3 and number2 != number3  
print(result)

#homework 5
username = input("enter your name: ")
password = input("enter your password: ")

correct_username = "admin"
correct_password = "12345"

result = (username == correct_username) and (password == correct_password)

print(result)
