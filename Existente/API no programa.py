import requests
import json

API_sei = "93b1b6e8e66e5189857e04a698a778d7"
cidade = "Paris"
# por avanço português %20 Rio%20de%20Janeiro Rio de Janeiro
endereço = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_sei}&lang=pt_br"

requisição = requests.get(endereço)
requisição_dic = requisição.json()
descrição = requisição_dic['weather'][0]['description']
temperatura = requisição_dic['main']['temp'] - 273.15
tor = requisição_dic['coord']['lon']
ter = requisição_dic['coord']['lat']
tir = requisição_dic['name']

print(descrição, f"{tir} {temperatura}ºC {tor} longitude {ter} latitude")
print(endereço)
print(requisição.json())
