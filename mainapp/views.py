from django.shortcuts import render,HttpResponse
from .config import *
from binance.client import Client
import time
client = Client(API_KEY,API_SECRET)

# Create your views here.
def StockPicker(request):
	info = client.get_all_tickers()
	data = []
	for i in info:
		data.append(i['symbol'])

	context = {'data':data}
	return render(request,'mainapp/stockpicker.html',context)
def StockTracker(request):
	stockpicker=request.GET.getlist('stockpicker')
	print(stockpicker)
	data={}
	data_1 = {}
	avaliable_stocks = client.get_all_tickers()
	for i in stockpicker:
		candles = client.get_klines(symbol=i,interval=Client.KLINE_INTERVAL_1MINUTE)[-1]
		
		candles_2=client.get_klines(symbol=i,interval=Client.KLINE_INTERVAL_1MINUTE)[-2]
	
		
		data.update({i:candles})
		data_1.update({i:candles_2})
		print(data)
		for key,value in data_1.items():
			for key_1 in data.keys():
				data[key_1].append(value[4])
				

		

	# print(data)
	# print(data_1)
	context = {'data':data,'room_name':'track'}
	return render(request,'mainapp/stocktracker.html',context)
