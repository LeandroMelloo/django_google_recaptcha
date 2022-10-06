from django.urls import path
from recaptcha_runner import views

urlpatterns = [
    path('', views.home, name='homepage'),
]
