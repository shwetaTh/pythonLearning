a= float(input("Enter number 1:"))
b= float(input("Enter number 2: "))
print("Select operation: ")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (x)")
print("4. Divide (/)")

oper = int(input("Enter your choice (1/2/3/4): "))

if oper==1:
    print(a+b)
elif oper==2:
    print(a-b)
elif oper==3:
    print(a*b)
elif oper==4:
    print(a/b)
else:
    print("Invalid number / operator. Please try again")