import math
sonlar=[]
for i in range(10, 0, -1):
    sonlar.append(i)
print(f"kamayish tartibidagi sonlar: {sonlar}".capitalize())
print(f"barcha sonlar {sonlar.count(4)} marta qatnashgan".title())
x=int(input("x sonini kirit = "))
y=int(input("y sonini kirit = "))
print(math.hypot(x,y))
print(math.log(x,y))
print(math.factorial(x))