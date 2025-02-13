def is_all_lowercase(s):
    return s.islower()

user_input = input("Enter a string: ")

result = is_all_lowercase(user_input)

print("The string is completely lowercase:", result)
