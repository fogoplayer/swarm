

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import main
import algorithm


from .models import Greeting


# General Notes:
# -the "request" parameter is a pull request from the client
# -you must tie each view to a url in the urls file

# index is the default or "home" webpage loaded when a client visits the url without a specified webpage
def index(request):
    template = loader.get_template('herokuTest/index.html')  # allow for a pretty webpage using html template

    return JsonResponse("Ping!", safe=False)


def json_input(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            #  TODO put code here to store data given from the client
    return HttpResponse(request.body)  # print the request as a HttpResponse


def json_output(request):  # TODO HIGH PRIORITY: IMPLEMENT
    return HttpResponse()


def greetings(request):  # I think this code is from some example, but i'm leaving it in to see what it does
    greeting = Greeting()  # Seems like it just stores the time of each visit and prints it out at the end
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, {'greetings': greetings})

#Actual routes------------------------------------------------------------------
def signup(request):
    #TODO access global server virtual lot and occupants array
    