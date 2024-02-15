num1 = 0
num2 = 1

given = int(input("Enter the range of the Fibonacci series: "))
print(num1)
print(num2)
a=range(1,given-1)
for i in a: 
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3