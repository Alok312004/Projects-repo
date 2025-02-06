import math
def calculate_expression(x,y,z):
    return 4 * (x**4) + 3 * (y**3) + 9 * z + 6 * math.pi

x = int(input("enter value of x "))
y = int(input("enter value of y "))
z = int(input("enter value of z "))

result = calculate_expression(x,y,z)

print(f"the result of expression is {result}")
