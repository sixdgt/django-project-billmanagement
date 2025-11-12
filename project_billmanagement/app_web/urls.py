from django.urls import path
from app_web.views import index, login

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
]