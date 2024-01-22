
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'post'

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('update/<int:pk>', update, name='update'),
    path('detail/<int:pk>', detail, name='detail'),
    path('delete/<int:pk>', delete, name='delete'),
    path('like/', like, name='like'),
    path('comment/', comment, name='comment'),
    path('comment_delete/', comment_delete, name='comment_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)