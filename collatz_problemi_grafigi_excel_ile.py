import openpyxl as xl
import matplotlib.pyplot as plt
import pandas as pd

# dosyayı oluşturma fonksiyonu
def xlCreate(filename, title1, title2):
  xlfile = xl.Workbook() # dosyayı oluştur
  worksheet = xlfile.active # çalışma sayfasını aç
  worksheet['A1'] = title1 # hücreleri elimizle girebiliyoruz
  worksheet['B1'] = title2
  xlfile.save(filename) # dosyayı kaydet
  xlfile.close() # dosyayı kapat

# dosyaya yazma fonksiyonu
def xlWrite(step, num):
  xlfile = xl.load_workbook("collatz.xlsx") # var olan dosyayı aç
  worksheet = xlfile.active # çalışma sayfasını aç
  worksheet.append([step, num]) # son satıra veriyi ekle
  xlfile.save("collatz.xlsx") # dosyayı kaydet
  xlfile.close() # dosyayı kapat

# collatz problemi
def collatz(arr):
  counter = 0
  for i in arr:
    tmp = i
    while i != 1:
      if i % 2 == 0:
        i /= 2
      else:
        i = (3 * i) + 1
      counter+=1
    xlWrite(counter, tmp) # çözümü excel dosyasına kaydet
    counter = 0

# grafik çizmek için fonksiyon
def drawGraph(filename, xlabel, ylabel, title):
  data = pd.read_excel(filename) # dosyayı oku
  plt.figure(figsize = (10,4)) # grafiğin boyutlarını belirle
  # grafiği çiz, ilk değişken x ekseni, ikinci değişken y ekseni, geri kalanı süsleme
  plt.plot(data.Sayilar, data.AdimSayisi, color = "#fd8d3c", linewidth = 2, 
    linestyle = "--", marker = "o", markersize = 7, markerfacecolor = "orange")
  plt.xlabel(xlabel) # x ekseni başlığı
  plt.ylabel(ylabel) # y ekseni başlığı
  plt.title(title) # grafiğin başlığı
  plt.grid(alpha = 0.3, linestyle = ":") # ızgara çiz
  plt.show() # grafiği göster

# dosyayı oluşturuyorum
xlCreate("collatz.xlsx", "AdimSayisi", "Sayilar")
# 1-50 arası sayılar için collatz problemini çözmek istiyorum
# o yüzden 1-50 arası bir dizi oluşturuyorum
arr = [x for x in range(1,51)]
# problemi 1-50 arasındaki sayılar için çözüp dosyaya kaydediyorum
collatz(arr)
# grafiği çizdiriyorum
drawGraph("collatz.xlsx", "Sayılar", "Adım Sayısı", "Collatz Problemi")