import urllib.request
import requests
opener = urllib.request.build_opener()

response = opener.open ("https://httpbin.org/get")
print(response.read())


response = requests.get("https://httpbin.org/get")
print(response.content)

# response = opener.open ("https://httpbin.org/")
# print(response.read())
print("*"*40)

response = requests.get("https://httpbin.org/")
response = requests.get("http://127.0.0.1:5500/index.html")
print(response.text)


# task1
# Виконайте вибірку (скрапінг) всіх заголовків (наприклад, h2) 
# із сайту http://kreatech.lviv.ua/news/.

# HomeWork day9
# Завдання
# Зайдіть на сайт національного банку вашої країни та знайдіть інформацію про курс валют.
# Здійсніть парсинг цієї сторінки та дістаньте курс долара США.
# На основі отриманої інформації реалізуйте конвертер валют.
# Після запуску програми користувач вводить у консоль кількість валюти своєї країни, 
# а в результаті на екран виводиться відповідна їй сума в доларах США. 