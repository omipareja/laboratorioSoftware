from django.urls import path
from . import views
app_name = 'salas'
urlpatterns = [
    path('chat/', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]