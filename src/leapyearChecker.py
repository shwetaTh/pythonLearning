def is_leap(year):
    leap = False
    
    if year%4==0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    
    return leap

year = int(input("enter the year: "))

if is_leap(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")