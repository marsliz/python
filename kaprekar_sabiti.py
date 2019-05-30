# Küçükten büyüğe
def asc(n):
    return int(''.join(sorted(str(n))))

# Büyükten küçüğe
def desc(n):
    return int(''.join(sorted(str(n))[::-1]))

# Sayı alalım
n = int(input("Sayı girin: "))

# Sayı 4 haneli mi kontrol edelim
if len(str(n))==4:

    # Doğru sonuç almamız için sayımızı kontrol edelim
    if n > 1000 and n < 9999:

        # Hesaplamaları yapalım
        print("\nHesaplanıyor...", n)
        while n != desc(n) - asc(n):
            print (desc(n), "-", asc(n), "=", desc(n)-asc(n))
            n = desc(n) - asc(n)

        # Sonucu ekrana yazdıralım
        if n == 0:
            print("Sayınız uygun değil, lütfen kurallara uygun bir sayı seçin!")
        else:
            print("Kaprekar sabiti:", n)
    else:
        print("1000'den büyük 9999'dan küçük bir sayı giriniz!")
else:
    print("4 haneli bir sayı giriniz!")