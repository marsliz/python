def kaprekar_number(sayi):
    karesi = str(sayi ** 2)
    yarisi = int(len(karesi) / 2)
    if yarisi == 0:
        return sayi == karesi
    elif yarisi > 0:
        sol = int(karesi[:yarisi])
        sag = int(karesi[yarisi:])
        toplam = sol + sag
        print("\n", sayi, "x", sayi, "=", karesi, "\n", sol, "+", sag, "=", toplam, "\n")
        return sayi == sol + sag

sayi = int(input("Sayı giriniz: "))

if sayi == 1:
    print(sayi,"kaprekar sayısıdır.")
elif kaprekar_number(sayi) == True:
    print(sayi,"bir kaprekar sayısıdır.")
else:
    print(sayi,"kaprekar sayısı değildir.")