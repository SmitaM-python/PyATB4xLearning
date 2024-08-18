"""
Program to do maths operations
Format output in string format
"""
num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))

max_num = max(num1, num2)
print("max num is ",f"{max_num}")

power = pow(num1, num2)
print("power is ",f"{power}")

sum = num1+num2
print("Sum is " , f"{sum}")

sub = num1-num2
print("Sub is " , f"{sub}")

mul = num1*num2
print("Mul is " , f"{mul}")

div = num1/num2
print("Div is " , f"{div}")