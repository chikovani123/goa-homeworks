def list_join(user_list, str_to_join):
    result = str_to_join.join(user_list)
    print(f"result: {result}")

list_join(["oragne", "lemon", "apple"], ", ")
list_join(["Hello", "world"], " ")
list_join(["goa", "is", "cool"], "-")
