from django.urls import path
from . import views

app_name ='mpesa_api'

urlpatterns = [
    path('', views.index, name='index'),
    path('records/', views.records, name='records')
]