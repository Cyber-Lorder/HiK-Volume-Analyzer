import os
from time import sleep
import pandas as pd, csv ,json

from binance.client import Client
from binance.websockets import BinanceSocketManager
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



