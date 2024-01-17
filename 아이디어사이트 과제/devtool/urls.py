from django.urls import path
from .views import *

app_name = 'devtool'

urlpatterns = [
    path('devList/', dev_list, name='dev_list'),
    path('devCreate/', dev_create, name='dev_create'),
    path('devUpdate/<int:pk>', dev_update, name='dev_update'),
    path('devDetail/<int:pk>', dev_detail, name='dev_detail'),
    path('devDelete/<int:pk>', dev_delete, name='dev_delete'),
]