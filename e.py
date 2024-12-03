# Uchta sonni o'qiydigan va faqat musbat sonlarning yig'indisini hisoblaydigan dastur yozing.
a=int(input("a sonini kirit = "))
b=int(input("b sonini kirit = "))
c=int(input("c sonini kirit = "))
if a>0 and b>0 and c>0:
    print(a+b+c)
elif a>0 and b>0 and c<0:
    print(a+b)
elif a>0 and b<0 and c>0:
    print(a+c)
elif a<0 and b>0 and c>0:
    print(b+c)
elif a>0 and b<0 and c<0:
    print(a)
elif a<0 and b>0 and c<o:
    print(b)
elif a<0 and b<0 and c>0:
    print(c)
else:
    print("kiritgan soningiz manfiy bo'lishi mumkin")
