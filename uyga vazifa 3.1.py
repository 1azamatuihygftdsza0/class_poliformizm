hafta_kunlar=['dushanba','seshanba','chorshanba','payshanba','juma','shanba','yakshanba']
x=int(input("1 va 7 oralig'idagi sonni kiriting = "))
if x>=1 and x<=7:
    print(hafta_kunlar[x])
else:
    print("xato")