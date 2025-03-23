def BONUS(arr):
    odd_numbers = [num for num in arr if num % 2 == 1]  
    even_numbers = [num for num in arr if num % 2 == 0]  
    even_numbers.reverse() 
    return odd_numbers + even_numbers 

print(BONUS([1, 2, 3, 4, 5, 6, 7, 8]))  
print(BONUS([10, 15, 20, 25, 30])) 
print(BONUS([2, 4, 6, 8]))         
print(BONUS([1, 3, 5, 7]))          
