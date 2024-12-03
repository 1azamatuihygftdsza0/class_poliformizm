import math

def main():
    material_ogirligi= float(input("Material og'irligini kiriting (kg) = "))
    qazish_samaradorligi = float(input("Ekstraktsiya samaradorligini kiriting (0-1) = "))

    olingan_mahsulot = material_ogirligi * qazish_samaradorligi

    butun_qismi = math.floor(olingan_mahsulot)
    fraksiyonel_mahsulot = olingan_mahsulot - butun_qismi

    print(f"Ekstraktsiyalangan mahsulot miqdori: {olingan_mahsulot:.2f} kg")
    print(f"Butun mahsulot: {butun_qismi} kg")
    print(f"Qism mahsulot: {fraksiyonel_mahsulot:.2f} kg")

    if olingan_mahsulot < 1:
        print("mahsulot kam, uni oshirish kerak.")
    elif olingan_mahsulot > 5:
        print("mahsulot juda ko'p, nazorat qilish kerak.")
    else:
        print("mahsulot miqdori qoniqarli.")
if __name__ == "__main__":
    main()