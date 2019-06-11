from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
        #домашняя страница
        path('login/',LoginView.as_view(template_name='users/login.html'), name='login'), ] 
