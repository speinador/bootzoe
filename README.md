# 🌐 BootZoe

Este script en Python publica automáticamente en Twitter la cotización actual de una la criptomoneda **ZOE**, utilizando los datos obtenidos desde la API de CoinMarketCap. Es útil para realizar un seguimiento automatizado del valor de ZOE y compartirlo públicamente.

## 📌 Características

- Conexión a la API de CoinMarketCap para obtener información actualizada sobre criptomonedas.
- Filtra y obtiene la cotización de la criptomoneda con símbolo `ZOE`.
- Publica automát icamente en una cuenta de Twitter con un mensaje predefinido que incluye fecha, hora, cotización y hashtags relevantes.

## 🧰 Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [Cuenta de Twitter con acceso a la API de desarrollador](https://developer.x.com/en)
- [Claves de API de CoinMarketCap y Twitter](https://coinmarketcap.com/)

## 💾 Librerías necesarias

Puedes instalarlas con:

```bash
pip install requests tweepy
```

## ⚙️ Configuración
Twitter API: reemplaza los siguientes valores en el script por tus claves reales:

```bash
API_KEY = 'TU API KEY'
API_SECRET_KEY = 'TU API SECRET KEY'
ACCESS_TOKEN = 'TU ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'TU ACCESS TOKEN SECRET'

CoinMarketCap API: ya viene con una clave de ejemplo (X-CMC_PRO_API_KEY), pero puedes cambiarla por tu propia clave obtenida desde CoinMarketCap Developer Portal.
```

## 🛠 Uso
Ejecuta el script con:
```bash
python bootzoe.py
```
Esto publicará en tu cuenta de Twitter la cotización actual de ZOE.

## ⚠️ Advertencia
Este script incluye hashtags relacionados con un posible esquema Ponzi. Úsalo con responsabilidad, considerando el contexto y la legalidad de la información difundida.

---

## 🧑‍🏫 Autor

Explicación elaborada por [Sebastian Peinador](https://www.linkedin.com/in/sebastian-j-peinador/) para propósitos didácticos y de investigación en ciberseguridad ofensiva.

---

## 📄 Licencia

Este material se distribuye bajo la licencia [MIT](LICENSE).

---

> Si te resulta útil, ¡no olvides darle ⭐ al repo o compartirlo!
