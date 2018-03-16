import requests


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader


from .models import Greeting


# Create your views here.
def index(request):
    cars = [
        [0, "Truck", "wait"],
        [1, "Sports Car", "Turn left"],
        [2, "MiniVan", "Back out and head to your left"],
        [3, "Bus", "wait"],
    ]
    template = loader.get_template('herokuTest/index.html')

    return JsonResponse(cars, safe=False)


def save_events_json(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
    return HttpResponse(request.body)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})