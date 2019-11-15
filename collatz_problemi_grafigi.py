import matplotlib.pyplot as plt
import pandas as pd

# adım sayısını ve sayıları sözlüğe eklemek için fonksiyon
def add(dic, step, num):
  dic.setdefault("AdimSayisi", []).append(step)
  dic.setdefault("Sayilar", []).append(num)

# collatz problemi
def collatz(dic, arr):
  counter = 0
  for i in arr:
    tmp = i
    while i != 1:
      if i % 2 == 0:
        i /= 2
      else:
        i = (3 * i) + 1
      counter+=1
    add(dic, counter, tmp) # adım sayısını ve sayıyı sözlüğe ekliyorum
    counter = 0

# grafik çizmek için fonksiyon
def drawGraph(dic, xlabel, ylabel, title):
  data = pd.DataFrame(dic) # verileri oku
  plt.figure(figsize = (10,4)) # grafiğin boyutlarını belirle
  # grafiği çiz, ilk değişken x ekseni, ikinci değişken y ekseni, geri kalanı süsleme
  plt.plot(data.Sayilar, data.AdimSayisi, color = "#fd8d3c", linewidth = 2, 
    linestyle = "--", marker = "o", markersize = 7, markerfacecolor = "orange")
  plt.xlabel(xlabel) # x ekseni başlığı
  plt.ylabel(ylabel) # y ekseni başlığı
  plt.title(title) # grafiğin başlığı
  plt.grid(alpha = 0.3, linestyle = ":") # ızgara çiz
  plt.show() # grafiği göster

# verileri tutmak için bir sözlük oluşturuyorum
dictionary = {}
# 1-50 arası sayılar için collatz problemini çözmek istiyorum
# o yüzden 1-50 arası bir dizi oluşturuyorum
arr = [x for x in range(1,51)]
# problemi 1-50 arasındaki sayılar için çözüp sözlüğe kaydediyorum
collatz(dictionary, arr)
# grafiği çizdiriyorum
drawGraph(dictionary, "Sayılar", "Adım Sayısı", "Collatz Problemi")