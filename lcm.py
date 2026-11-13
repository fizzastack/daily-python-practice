
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = abs(a)
y = abs(b)

if x == 0 or y == 0:
    print("LCM: 0")
else:
    num1 = x
    num2 = y

    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder

    gcd = num1
    lcm = (x * y) // gcd

    print("LCM:", lcm)
