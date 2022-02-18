import requests
import time

import tweepy

from tweepy import OAuthHandler

API_KEY = 'TU API KEY'
API_SECRET_KEY = 'TU API SECRET KEY'
ACCESS_TOKEN = 'TU ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'TU ACCESS TOKEN SECRET'

# Configuracion de acceso con las credenciales
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Listos para hacer la conexion con el API
api = tweepy.API(auth)

headers = {
        'X-CMC_PRO_API_KEY': 'd138126f-f123-4b4a-af4f-3a4afaf181db',
        'Accepts': 'application/json'
        }

params = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
        }

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = params, headers = headers).json()

coins =  json['data']

for coin in coins:
        if coin['symbol'] == 'ZOE':

            fecha = time.strftime("%d/%m/%y")
            hora = time.strftime("%H:%M:%S")
            moneda = str(round(coin['quote']['USD']['price'],5))
            texto = 'Cotizacion de $ZOE para el dia ' + fecha + ' a las ' + hora + ' = USD '
            hashcat = '#GeneraciónZoe #ZoeCash #ZoeCrash #ZoeGate #ZoeApp #Ponzi #ponzischeme #Zoeponzi #OneCoin'

mensaje = texto + moneda + '\n' + '\n' + hashcat

api.update_status(mensaje)
