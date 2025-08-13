from django.shortcuts import render
import requests

def index(request):
    # Не забудьте вставить ваш ключ API от OpenWeatherMap
    api_key = 'YOUR_API_KEY_HERE'
    city = 'Tashkent' # Город по умолчанию

    # Если пользователь ввёл город в форме, используем его
    if request.method == 'POST':
        city = request.POST['city']

    # Формируем URL для запроса к API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=ru'
    
    weather_data = None
    error_message = None

    try:
        # Отправляем запрос и получаем ответ
        response = requests.get(url)
        response.raise_for_status() # Проверяем, успешен ли запрос
        data = response.json()

        # Формируем словарь с нужными нам данными
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            error_message = f'Город "{city}" не найден. Попробуйте снова.'
        else:
            error_message = f'Произошла ошибка: {http_err}'
    except Exception as err:
        error_message = f'Произошла непредвиденная ошибка: {err}'


    context = {'weather_data': weather_data, 'error': error_message}
    return render(request, 'main/index.html', context)