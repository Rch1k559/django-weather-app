# Import necessary libraries
from django.shortcuts import render  # Django's function to render templates
import requests  # Library to make HTTP requests

# Define the main view for the weather page
def index(request):
    # API key for OpenWeatherMap. 
    # It's recommended to store this in a more secure place, like environment variables.
    api_key = 'YOUR_API_KEY_HERE' 
    
    # Set a default city
    city = 'Tashkent'

    # Check if the request method is POST, which means the user has submitted the form
    if request.method == 'POST':
        # Get the city name from the form data
        city = request.POST['city']

    # Construct the URL for the OpenWeatherMap API request
    # We are requesting weather data for the specified 'city' in metric units and Russian language
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}&lang=ru'
    
    # Initialize variables to hold weather data and error messages
    weather_data = None
    error_message = None

    try:
        # Send a GET request to the OpenWeatherMap API
        response = requests.get(url)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status() 
        # Parse the JSON response from the API
        data = response.json()

        # Extract the required weather information from the JSON data
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }

    # Handle HTTP errors, such as 404 Not Found
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            error_message = f'City "{city}" not found. Please try again.'
        else:
            error_message = f'An HTTP error occurred: {http_err}'
    # Handle other potential exceptions during the request
    except Exception as err:
        error_message = f'An unexpected error occurred: {err}'

    # Prepare the context dictionary to pass to the template
    context = {'weather_data': weather_data, 'error': error_message}
    # Render the 'index.html' template with the context data
    return render(request, 'main/index.html', context)
