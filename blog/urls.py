from django.urls import path
from .views import create_post_view, post_list_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('new/', create_post_view, name='create_post'),
]