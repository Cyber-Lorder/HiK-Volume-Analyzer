import os
from time import sleep
import pandas as pd, csv ,json

from binance.client import Client

from twisted.internet import reactor

api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)


priceonly= client.get_symbol_ticker(symbol="BTCUSDT")
print(priceonly)

allveriSymbol= client.get_ticker(symbol="BTCUSDT")
print(allveriSymbol)
allveri=client.get_ticker()

with open('sembolleri ayırdı.csv', 'w', newline='') as f:
	wr = csv.writer(f)
	for line in allveri:
		wr.writerow(line)

with open('bütünveriler.csv', 'a', newline='', encoding='utf-8') as f:
	w = csv.writer(f, delimiter='\n')
	w.writerow(allveri) #Bilgileri CSV formatında yazdır.


#with open('bütünveriler.csv', 'r', ) as datafile:
#	print(datafile.read().split()[1::30])

with open('bütünveriler.csv','r') as f:
    # Printing Specific Part of CSV_file
    # Printing last line of second column
    lines = list(csv.reader(f, delimiter = ' ', skipinitialspace = True))

""""""
for i in range(len(lines)):
        print(lines[i][0])
for i in range(len(lines)):
        print(lines[i][1])
for i in range(len(lines)):
        print(lines[i][28])
for i in range(len(lines)):
		print(lines[i][29])

"""yukardaki kodlar ile bütünveriler.csv dosyasındaki verilerden sadece ihtiyacımız olan veri sütunlarını ayırabiliyorum"""


dosya = open('bütünveriler.csv', 'r')
csv_dosyasi = open('semboller.csv', 'a')
for satir in dosya:
    ilgili_sütun= satir.split(",")[0]
    csv_dosyasi.write(ilgili_sütun)
csv_dosyasi = open('volums.csv', 'a')
dosya = open('bütünveriler.csv', 'r')
for satir in dosya:
    ilgili_sütun= satir.split(",")[14]
    csv_dosyasi.write(ilgili_sütun)
csv_dosyasi = open('lastPrice.csv', 'a')
dosya = open('bütünveriler.csv', 'r')
for satir in dosya:
    ilgili_sütun= satir.split(",")[5]
    csv_dosyasi.write(ilgili_sütun)
"""yukardaki kodlarla ise bütünveriler.csvden ilgili sütündaki verileri alıp farklı bir csv dosyasına kaydedebiliyorum"""
