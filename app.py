import requests

# Замените 'YOUR_API_KEY' на ваш фактический API ключ
API_KEY = 'AIzaSyB-WcIhGE44RKrrDxrepTMf3vB-BiAzCko'

# URL для запроса к API Google
url = 'https://us-central1-aiplatform.googleapis.com/v1/projects'

# Параметры для запроса
payload = {
    'key': API_KEY
}

# Отправка запроса
response = requests.get(url, params=payload)

# Обработка ответа от API Google
if response.status_code == 200:
    # API-ключ рабочий
    print('API-ключ рабочий')
else:
    # API-ключ не рабочий
    print('API-ключ не рабочий')
