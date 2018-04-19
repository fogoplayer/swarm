

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import main


from .models import Greeting


# Create your views here.
def index(request):
    carColor = request[0]
    carType = request[1]
    carOrientation = request[2]
    for spot in main.virtualLot:
        print  # stub
        # add the car to the lot and return an ID and instructions
    template = loader.get_template('herokuTest/index.html')

    return JsonResponse("placeholder", safe=False)  # write code to return id and instructions


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
