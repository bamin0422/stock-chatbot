from django.urls import path
from . import views

urlpatterns = [
    path('', views.specialStock_list, name='specialStock_list'),
    path('', views.stockNews_list, name='stockNews_list'),
    path('', views.stockCommunity_list, name='stockCommunity_list'),
]
