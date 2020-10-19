from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '22829855'
API_KEY = '4rVkouFNKB3FjAHFVHSvcG7m'
SECRET_KEY = 'Hbp6O7Q9SOF1BK5IHBbRei9br6rk1MlW'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

with open("4.png", "rb") as f:
    image = f.read()

result = client.basicGeneral(image)
print(result)