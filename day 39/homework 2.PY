def is_all_uppercase(s):
    return s.isupper()

user_input = input("Enter a string: ")

result = is_all_uppercase(user_input)

print("The string is completely uppercase:", result)
