def element_remover(user_list, index_to_remove):
    if 0 <= index_to_remove < len(user_list):
        removed_element = user_list.pop(index_to_remove)
        print(f"removed element: {removed_element}")
        print(f"user list: {user_list}")
    else:
        print("entered index is wrong!")

element_remover([20, 50, 80, 40, 70], 2)
element_remover(["orange", "banana", "apple", "peach"], 1)
element_remover([1, 2, 3, 4, 5], 4)
