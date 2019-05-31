sayi = int(input("Sayı giriniz : "))
sayiStr = str(sayi)
toplam = 0

for basamak in sayiStr:
    toplam += int(basamak) ** len(sayiStr)
    print("  ",basamak,"^",len(sayiStr),"=",int(basamak) ** len(sayiStr))

basamak1 = int(sayiStr[0]) ** len(sayiStr)
basamak2 = int(sayiStr[1]) ** len(sayiStr)
basamak3 = int(sayiStr[2]) ** len(sayiStr)

print(basamak1,"+",basamak2,"+",basamak3,"=",toplam)

if (toplam == sayi):
    print(sayi,"bir armstrong sayısıdır.")
else:
    print(sayi,"bir armstrong sayısı değildir.")