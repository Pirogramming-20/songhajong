from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    path('create/', create, name='create'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
