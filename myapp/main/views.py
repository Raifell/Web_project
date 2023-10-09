from django.shortcuts import render
from .models import Book, User


def main_page(request):
    return render(request, 'main/main_index.html')


def table_one_page(request):
    data = {'data': Book.objects.all()}
    return render(request, 'main/table_one_index.html', context=data)


def table_two_page(request):
    data = {'data': User.objects.all()}
    return render(request, 'main/table_two_index.html', context=data)
