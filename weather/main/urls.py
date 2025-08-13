from django.urls import path
from . import views

# This list holds the URL patterns for the 'main' app.
urlpatterns = [
    # The root URL of the app is mapped to the 'index' view.
    # The name 'index' can be used to refer to this URL pattern in other parts of the Django project.
    path('', views.index, name="index")
]