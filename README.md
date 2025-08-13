# Django Weather App

- A simple web application built with Django that allows users to check the current weather in any city around the world using the OpenWeatherMap API.
- This project was created for educational purposes to demonstrate the fundamental principles of the Django framework, how to interact with external APIs, and how to build a simple user interface.

# Features

- Weather Search: Enter a city name to get real-time weather data.

- Data Display: Shows the temperature, a short weather description (e.g., "clear sky"), and a corresponding weather icon.

- Error Handling: Displays a user-friendly message if the city is not found or if another API error occurs.

- Simple UI: A clean and minimalist design for ease of use.

# Tech Stack

- Backend: Python, Django

- Frontend: HTML, CSS

- API: OpenWeatherMap API

- Libraries: requests (for making HTTP requests to the API)

# Installation and Setup

- Follow these steps to get the project running on your local machine.

# 1. Clone the Repository:
- git clone https://github.com/Rch1k559/django-weather-app.git
- cd django-weather-app

# 2. Create and Activate a Virtual Environment:

# On Windows:
- python -m venv venv
- venv\Scripts\activate

# On macOS / Linux:
- python3 -m venv venv
- source venv/bin/activate

# 3. Install Dependencies:
- pip install -r requirements.txt

# 4. Set up the API Key:
- Get your free API key from OpenWeatherMap.
- Open the main/views.py file and paste your key into the api_key variable:
# main/views.py

- api_key = 'PASTE_YOUR_API_KEY_HERE'

# 5. Apply Migrations:
- python manage.py migrate

# 6. Run the Development Server:
- python manage.py runserver

# 7. Open the Application:

- Navigate to http://127.0.0.1:8000/ in your web browser.
