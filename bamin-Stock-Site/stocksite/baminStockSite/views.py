from django.shortcuts import render
from django.utils import timezone
from .models import *


def specialStock_list(request):
    specialStocks = SpecialStock.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/specialStock_list.html', {'specialStocks': specialStocks})


def specialStock_list_detail(request):
    specialStocks = SpecialStock.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/speicalStock_list_detail.html', {'specialStocks': specialStocks})


def stockNews_list(request):
    stockNews = StockNews.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockNews_list.html', {'stockNews': stockNews})


def stockNews_list_detail(request):
    stockNews = StockNews.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockNews_list_detail.html', {'stockNews': stockNews})


def stockCommunity_list(request):
    stockCommunity = StockCommunity.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockCommunity_list.html', {'stockCommunity': stockCommunity})


def stockCommunity_list_detail(request):
    stockCommunity = StockCommunity.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'stockSite/stockCommunity_list_detail.html', {'stockCommunity': stockCommunity})


def home(request):
    stockCommunity = StockCommunity.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    stockNews = StockNews.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    specialStocks = SpecialStock.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    data = {'stockCommunity': stockCommunity,
            'stockNews': stockNews, 'specialStocks': specialStocks}
    return render(request, 'stockSite/home.html', {'data': data})
