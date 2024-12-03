import math
# g lugat yordamida C,H,O,A,W_f,S qiymatini olamiz ular berilgan yoqilg'i tarkiblari
g={"C": int(input("C moddaning ulushi (%)da = ")), "O": int(input("O moddaning ulushi (%)da = ")),
    "H": int(input("H moddaning ulushi (%)da  = ")), "W_f": int(input("W_f moddaning ulushi (%)da  = ")),
   "S": int(input("S moddaning ulushi (%)da = "))}
Q_p=float(input("Q_p issiqlik miqdorini kiriting (J)da = "))
L_o=float(input("L_o 1 kg yoqilg'i uchun ketadigan havo miqdori (m^3)da = "))
V_o=float(input("V_o yoqilg'i hajmini kiriting (m^3)da = "))# V_o normal sharoitdagi hajm
a=float(input("a suyuq yoqilg'i uchun ortiqchalik koeffitsiyentini kiriting = "))
L=a*L_o
V=a*V_o
# W yoqilg'ining purkash uchun uzatilayotgan purkagich bug' sarfi
W=float(input("W yoqilg'ining purkash uchun uzatilayotgan bug' sarfi (kg/m^3)da = "))
G=1+a*L_o+W
# 1kg yoqilg'i to'liq yonishida kerak bo'ladigan massa: m_1,m_2,m_3,m_4,m_5
m_1=3667*g["C"]/100000
m_2=9*g["H"]/100+1*g["W_f"]/100+W
m_3=768*a/1000*L_o+g["S"]
m_4=L_o*(a-1)*232/1000
m_5=2*g["S"]/100
# h ro'yxat tegishli ravishda  m_1,m_2,m_3,m_4,m_5 larning molyar massalari
h=[int(input("M_1 ning molyar massasi (g/mol)da = ")),int(input("M_2 ning molyar massasi (g/mol)da = ")),
   int(input("M_3 ning molyar massasi (g/mol)da = ")),int(input("M_4 ning molyar massasi (g/mol)da = ")),
   int(input("M_5 ning molyar massasi (g/mol)da = "))]
V_1=m_1*22.4/h[0]
V_2=m_2*22.4/h[1]
V_3=m_3*22.4/h[2]
V_4=m_4*22.4/h[3]
V_5=m_5*22.4/h[4]
V_umumiy=V_1+V_2+V_3+V_4+V_5
ro=G/V_umumiy
# k ro'yxati tegishli ravishda m_1,m_2,m_3,m_4,m_5 larning solishtirma issiqlik sig'imi
k=[int(input("q_1 solishtirma issiqlikni kiriting (J/(mol*k)da = ")),int(input("q_2 solishtirma issiqlikni kiriting (J/(mol*k)da = ")),
   int(input("q_3 solishtirma issiqlikni kiriting (J/(mol*k)da = ")),int(input("q_4 solishtirma issiqlikni kiriting (J/(mol*k)da = ")),
   int(input("q_5 solishtirma issiqlikni kiriting (J/(mol*k)da = "))]
# I mahsulotlarning entalpiyalari
I=m_1*k[0]+m_2*k[1]+m_3*k[2]+m_4*k[3]+m_5*k[4]
Q_m=I/Q_p
# etta o'txonaning foydali ish koeffitsiyenti
etta=1-Q_m  # etta o'txonaning foydali ish koeffitsiyenti
# Q_foy o'txonaning foydali issiqlik yuklamasi
Q_foy=Q_p*g["C"]*g["H"]
C_k=(m_1*k[0]+m_2*k[1]+m_3*k[2]+m_4*k[3]+m_5*k[4])/G
B=Q_foy/(Q_p*etta)
q_s=float(input("q_s ni interpolitsiyadan foydalanib kiriting (Vt/m^3)da = "))
H_s=B*Q_p*etta/q_s
fi=float(input("fi ya'ni a ga bog'liq holda o'zgargan koeffitsiyentni kiriting = "))
H_l=H_s/fi
K=float(input("K shakl omilini kiriting Vt/(m^2*K)da = "))
h=H_l/K
l_t=float(input("l_t radiant truba uzunligini kiriting (m)da = "))
l_p=l_t-0.5
a_k=0.848 # a_k proporsionallik koeffitsiyenti
f=(a_k-0.5)*l_p
U=G/f
E=float(input("E harorat koeffitsiyentini kiriting  = "))
d_p=float(input("d_p kamera trubasining uzunligini kiriting (m)da = "))
a_l=0.35*E*math.pow(U,0.6)/math.pow(d_p,0.4)
t=int(input("t o'rtacha haroratni kiriting (selsiyda)= ")) # o'rtacha harorat
a_n=0.0256*t-2.33
M=1.1*(a_l-a_k)
H_n=Q_p/(M*t)
q_k=Q_p/H_n
if q_k>4000:
   print(f"Konveksion trubalarga tavsiya etilgan issiqlik kuchlanishi = {q_k} kVt/m^2 .")
else:
   print("Issiqlik kuchlanishi yetarli emas")
print(f"yoqilg'ining haqiqiy sarfi = {L} kg/m^3".capitalize())
print(f"yoqilg'ining normal sharoitdagi sarfi = {V} m^3/kg".capitalize())
print(f"yonish mahsulotlarining normal sharoitdagi zichligi = {ro} kg/m^3 ga teng")
print(f"Yonish maahsulotlarininG entalpiyalari = {I} kJ/kg".lower())
print(f"                  O'txonadan chiqib ketayotgan tutun gazlari bilan issiqlik yo'qotilishi = {Q_m}".lstrip())
print(f"1 kg yoqilg'i yonishida hosil bo'ladigan yonish MAHSULOTLARI = {G} kg".lower())
print(f"Yoqilg'ining bir soatdagi sarfi = {B} kg/soat")
print(f"Yonish mahsulotlarining o'rtacha issiqlik sig'imi = {C_k} kJ/(kg*K)".capitalize())
print(f"                 O'txonaning foydali issiqlik yuklamasi = {Q_foy} kJ/soat                 ".strip())
print(f"Dbsolyut qora jism yuzasiga ekvivalent yuza = {H_s} m^2".replace('D','A'))
print(f"yuzning quyosh yutish samaradorligi = {H_l}".replace('quyosh','nur'))
print(f"trubalarni o'rnini bosadigan, ekranlashtirilgan yassi yuzaning qiymati = {h} m^2")
print(f"Mevosita tutun gazlari bilan yuvilib turuvchi trubalarning foydali uzunligi = {l_p} m".replace('M','B'))
print(f"                Massaviy tezlik = {U} kg/(m^2*s) ".lstrip())
print(f"erkin ko'ndalanG kesim yuzasi = {f} m^2".lower())
print(f"Nurlanish paytida issiqlik berish koeffitsiyenti = {a_n}         ".strip())
print(f"tutun gazlaridan trubalarga issiQlik berish koeffitsiyenti = {a_l}".lower())
print(f"isitish uchun zarur konveksion trubalarning yuzasi = {H_n} m^2".capitalize())














