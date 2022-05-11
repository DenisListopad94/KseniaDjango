from django.http import HttpResponse
from django.shortcuts import render


def main_page(request):
    return HttpResponse("Hello Django")

def super_car(request):
    return render(request,"Car/cars.html")