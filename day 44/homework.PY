# 1) 
def first_and_last(lst):
    if not lst:
        return None  
    return [lst[0], lst[-1]]

# 2) 
def max_of_three(a, b, c):
    return max(a, b, c)

# 3) 
def reverse_string(s):
    return s[::-1]

# BONUS
def reverse_string_no_slice(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  
    return reversed_s

print(first_and_last([1, 2, 3, 4]))  
print(max_of_three(10, 25, 15))  
print(reverse_string("hello")) 
print(reverse_string_no_slice("hello"))  
