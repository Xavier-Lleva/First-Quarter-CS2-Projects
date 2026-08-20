import math 

x1, x2 = map(int, input("Enter the two x points (x1 x2): ").split())
y1, y2 = map(int, input("Enter the two y points (y1 y2): ").split())

c1 = (x2 - x1)
c2 = (y2 - y1)
d = math.sqrt((math.pow(c1, 2))+(math.pow(c2, 2)))

print(f"Distance: {d:.2f}")