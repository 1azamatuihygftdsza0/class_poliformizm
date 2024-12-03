# mukammal sonni toping Masalan: 6 murakkab son
while True:
    a=int(input(" a sonini kiriting = "))
    k=0
    for i in range(1,a):
        if a%i==0:
            k += i
    if a==0:
        break
    elif a==k:
        print("True")
    else:
        print("False")


