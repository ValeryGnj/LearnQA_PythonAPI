import requests

# Отправляем первый запрос для получения куки
payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

# Получаем значение куки
cookie_value = response1.cookies.get('auth_cookie')

# Создаем словарь с куками
cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

# Отправляем второй запрос с использованием куки
response2 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", cookies=cookies)

print(response2.text)
