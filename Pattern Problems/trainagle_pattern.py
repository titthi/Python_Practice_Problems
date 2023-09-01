rows = int(input("Enter the number of rows: \n "))

# right triangle star pattern
for i in range(0,rows):
    for j in range(0,i+1):
        print("*", end = '')
    print()

# mirrored right triangle star pattern
for i in range(1,rows+1):
    for j in range(1,rows-i+1):
        print(" ", end = '')
    for k in range(0,i):
        print("*", end = '')
    print()

# Right down mirrored triangle star pattern
for i in range(1,rows+1):
    for j in range(1,i):
        print(' ', end = '')
    for k in range(i,rows+1):
        print("*", end = '')
    print()

# Left Triangle Star Pattern
for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print("*", end = '')
    print()