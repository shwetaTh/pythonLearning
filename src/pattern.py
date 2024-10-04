n = int(input("Enter range: "))
# i=1
# while i<=n:
#     for _ in range(i):
#         print("*", end='')
#     print()
#     i+=1

# i=n
# while i>=1:
#     for _ in range(i):
#         print("*", end='')
#     print()
#     i-=1  


i = 1  # Start with the first row
while i <= n:
    # Print spaces (n - i) spaces
    for _ in range(n - i):
        print(" ", end='')
    
    # Print asterisks (2 * i - 1) asterisks
    for _ in range(2 * i - 1):
        print("*", end='')
    
    # Move to the next line after printing spaces and asterisks
    print()
    
    i += 1  # Move to the next row                 