num = int(input("Enter a number: "))
i = num
fact = 1
while i>0:
    fact*=i
    i-=1

print(f"The factorial of {num} is {fact}")    