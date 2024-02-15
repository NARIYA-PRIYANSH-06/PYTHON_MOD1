num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

def sum(num1,num2,num3):
    if num1==num2 or num2==num3 or num3==num1:

        return 0 
    else:

        return num1+num2+num3

result = sum(num1,num2,num3)
print("sum of integer is : ",result)