import requests
import json

#Consumir API
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
#Transformar formato
cotacoes = cotacoes.json()

#Definir as cotações
cotacao_dolar = cotacoes['USDBRL']["bid"]
cotacao_euro = cotacoes['EURBRL']["bid"]
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

#Informar cliente
print("O valor do Dólar neste momento é de ", cotacao_dolar, "reais")
print("O valor do Euro neste momento é de ", cotacao_euro, "reais")
print("O valor do Bitcoin neste momento é de ", cotacao_bitcoin, "reais")