


line = "(25,4) (1,-6)"

line1, line2 = line.split(" ")

lx1, ly1 = line1.split(",")
lx2, ly2 = line2.split(",")

x1 = int(lx1[1:len(lx1)])
y1 = int(ly1[0:len(ly1)-1])

x2 = int(lx2[1:len(lx2)])
y2 = int(ly2[0:len(ly2)-1])

print(line1)
print(x1, y1)
print(x2, y2)