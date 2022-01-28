from celery import shared_task
from binance.client import Client
from .config import *

client = Client(API_KEY,API_SECRET)

@shared_task(bind=True)
def update_stock(self,stockpicker):
	data={}
	data_1 = {}
	# avaliable_stocks = client.get_all_tickers()
	for i in stockpicker:
		candles = client.get_klines(symbol=i,interval=Client.KLINE_INTERVAL_1MINUTE)[-1]
		
		candles_2=client.get_klines(symbol=i,interval=Client.KLINE_INTERVAL_1MINUTE)[-2]
	
		
		data.update({i:candles})
		data_1.update({i:candles_2})
		print(data)
		for key,value in data_1.items():
			for key_1 in data.keys():
				data[key_1].append(value[4])
				

		
	return 'Done'
	# print(data)
	# print(data_1)
	
