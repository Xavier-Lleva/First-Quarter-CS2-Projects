import math

x1, x2 = map(int, input("Enter the two x points (x1 x2): ").split())
y1, y2 = map(int, input("Enter the two y points (y1 y2): ").split())

p1 = (x1, y1)
p2 = (x2, y2)
d = math.dist(p1, p2)

print(f"Distance: {d:.2f}")