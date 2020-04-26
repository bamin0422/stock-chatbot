from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('specialstock/', views.specialStock_list, name='specialStock_list'),
    path('specialstock_detail/', views.specialStock_list_detail,
         name='specialStock_list_detail'),
    path('stocknews/', views.stockNews_list, name='stockNews_list'),
    path('stocknews_detail/', views.stockNews_list_detail,
         name='stockNews_list_detail'),
    path('stockcommunity/', views.stockCommunity_list, name='stockCommunity_list'),
    path('stockcommunity_detail/', views.stockCommunity_list_detail,
         name='stockCommunity_list_detail'),

]
