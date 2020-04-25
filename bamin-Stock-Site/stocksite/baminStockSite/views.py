from django.shortcuts import render
from django.utils import timezone
from .models import *


def specialStock_list(request):
    specialStocks = SpecialStock.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/specialStock_list.html', {'specialStocks': specialStocks})


def stockNews_list(request):
    stockNews = StockNews.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockNews_list.html', {'stockNews': stockNews})


def stockCommunity_list(request):
    stockCommunity = StockCommunity.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockCommunity_list.html', {'stockCommunity': stockCommunity})
