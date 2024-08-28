from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Это первая большая корзина цветов для вас!</h1>")

def data(request):
    return HttpResponse("<h1>Это вторая большая корзина цветов для мамы!</h1>")


def test(request):
    return HttpResponse("<h1>Пройдите тест и определите какие цветы подходят вам больше всего!</h1>")