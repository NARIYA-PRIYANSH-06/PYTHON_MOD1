def check_values(num1, num2):
        return num1 == num2 or num1 + num2 == 5 or abs(num1 - num2) == 5

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

result = check_values(num1, num2)
print(f"The result is: {result}")