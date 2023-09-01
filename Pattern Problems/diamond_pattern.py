rows = int(input("Enter number of rows: \n"))

for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(' ', end = '')
    for k in range(rows-i+1, rows+i):
        print("*", end = '')
    print()

for i in range(1,rows):
    for j in range(1,i+1):
        print(' ', end = '')
    for k in range(i+1, 2*rows-i ):
        print("*", end = '')
    print()

