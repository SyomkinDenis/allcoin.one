from django.shortcuts import render
import requests
from django.http import JsonResponse


def index(request):
    crypto_name = [
        'BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'XRPUSDT', 'ETCUSDT',
        'BNBUSDT', 'ADAUSDT', 'DOGEUSDT', 'TRXUSDT', 'LINKUSDT',
        'AVAXUSDT', 'DOTUSDT', 'MATICUSDT', 'LTCUSDT', 'UNIUSDT',
        'SHIBUSDT', 'BCHUSDT', 'XMRUSDT',
        ]
    crypto_price = save_price_binance(crypto_name)
    crypto_price_dict = dict(zip(crypto_name, crypto_price))
    data = {"crypto_name": crypto_name, "crypto_price_dict": crypto_price_dict}
    return render(request, "index.html", data)

def save_price_binance(arg):
    crypto_price = []
    # Формируем список цены и валюты
    for i in arg:
        crypto_price.append(float(get_price_binance(i)))
    return crypto_price

def get_price_binance(symbol):
    # URL эндпоинта Binance для получения цены криптовалюты
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": symbol
    }
    # Отправляем GET-запрос к API Binance
    response = requests.get(url, params=params)
    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()     
        # Извлекаем цену криптовалюты из ответа
        if 'symbol' in data and 'price' in data:
            crypto_price = data['price']
            return crypto_price
        else:
            return None
    else:
        return None
