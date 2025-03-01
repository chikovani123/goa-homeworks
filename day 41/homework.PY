# 2) 
def greet():
    print("Hello, World!")

# 3) 
def add_numbers(a, b):
    print(a + b)

# 4)
def multiply_by_ten(n):
    return n * 10
# 5)
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

# 6)
def outer_function():
    def inner_function():
        print("Inner function called")
    inner_function()

# 7)
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

# 8) Find the Maximum
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# 9) 
def filter_positive(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers
# 10)
def sum_divisible_by_3(start=1, end=100):
    total = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total += num
    return total

greet()
add_numbers(5, 7)
print(multiply_by_ten(4))
greet_person()
greet_person("Alice")
outer_function()
check_even_odd([1, 2, 3, 4, 5])
print(find_max([10, 20, 30, 5, 25]))
print(filter_positive([-5, 10, -3, 8, 0, 15]))
print(sum_divisible_by_3())
