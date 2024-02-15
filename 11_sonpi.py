def sum_of_positive_integers(n):

    if n <= 0:
        return "Please enter a positive integer."
    
    total_sum = sum(range(1, n+1))
    
    return total_sum

n = int(input("Enter a positive integer (n): "))

result = sum_of_positive_integers(n)
print(f"The sum of the first {n} positive integers is: {result}")