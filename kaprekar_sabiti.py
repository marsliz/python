# K���kten b�y��e
def asc(n):
    return int(''.join(sorted(str(n))))

# B�y�kten k����e
def desc(n):
    return int(''.join(sorted(str(n))[::-1]))

# Say� alal�m
n = int(input("Say� girin: "))

# Say� 4 haneli mi kontrol edelim
if len(str(n))==4:

    # Do�ru sonu� almam�z i�in say�m�z� kontrol edelim
    if n > 1000 and n < 9999:

        # Hesaplamalar� yapal�m
        print("\nHesaplan�yor...", n)
        while n != desc(n) - asc(n):
            print (desc(n), "-", asc(n), "=", desc(n)-asc(n))
            n = desc(n) - asc(n)

        # Sonucu ekrana yazd�ral�m
        if n == 0:
            print("Say�n�z uygun de�il, l�tfen kurallara uygun bir say� se�in!")
        else:
            print("Kaprekar sabiti:", n)
    else:
        print("1000'den b�y�k 9999'dan k���k bir say� giriniz!")
else:
    print("4 haneli bir say� giriniz!")