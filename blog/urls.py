from django.urls import path, include
from blog import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/create/', views.post_create, name='post_create'),
    path('detail/', views.detail, name='detail'),
    path('test/', views.test, name='test'),
]