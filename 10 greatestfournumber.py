# WAP to find the greatest of four number
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))
num4 = int(input("Enter the number: "))

if(num1>num2 and num1>3 and num1>4):
    print("The greatest number is",num1)

elif(num2>num1 and num2>3 and num2>4):
    print("The greatest number is",num2)

elif(num3>num1 and num3>2 and num3>4):
    print("The greatest number is",num3)

elif(num4>num1 and num4>2 and num4>3):
    print("The greatest number is",num4)

else:
    print("All numbers are equal")

 

