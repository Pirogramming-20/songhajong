from django.urls import path, include
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', idea_list, name='idea_list'),
    path('ideaSubmit/', idea_submit, name='idea_submit'),
    path('ideaDetail/<int:pk>', idea_detail, name='idea_detail'),
    path('ideaUpdate/<int:pk>', idea_update, name='idea_update'),
    path('ideaDelete/<int:pk>', idea_delete, name='idea_delete'),
]
