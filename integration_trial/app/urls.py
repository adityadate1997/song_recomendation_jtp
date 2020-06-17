from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('searchResults/', views.searchResults, name='searchResults'),
    path('searchResults/result/', views.result, name='result')
]
