'''
This must be executed from fogoplayer.github.io/swarm so jQuery works properly

$.getJSON('https://swarm-edd.herokuapp.com/signup', {
            carColor: "Blue",
            carType: "Sedan",
            carOrientation: "backwards",
            carLocation: navigator.geolocation.getCurrentPosition(function(position) {
                return [42.3461949, 83.4919403];
            })
        }, function(data) {
            console.log(data.instructions);                                     //Expected return: ["Go fast", "Turn left"]
        });
'''

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import Server.lot as lot
import algorithm
from .models import Greeting
import Server.manager as lotManager


# Create your views here
def index(request):
    return render(request, "base.html")


# General Notes:
# -the "request" parameter is a pull request from the client
# -you must tie each view to a url in the urls file

def json_input(request):
    if request.is_ajax():
        if request.method == 'POST':
            print('Raw Data: "%s"' % request.body)
            #  TODO put code here to store data given from the client
    return HttpResponse(request.body)  # print the request as a HttpResponse


def json_output(request):  # TODO HIGH PRIORITY: IMPLEMENT
    return JsonResponse("Here is a json response!", safe=False)


def greetings(request):  # I think this code is from some example, but i'm leaving it in to see what it does
    greeting = Greeting()  # Seems like it just stores the time of each visit and prints it out at the end
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, {'greetings': greetings})


# Actual routes------------------------------------------------------------------
def signup(request):
    print(1)
    occupants = lotManager.getOccupants()
    print(2)
    vLot = lotManager.getLot()
    print(3)
    print(request)
    userCoords = lot.getVlotCoordinates(request.body.carLocation[0], request.body.carLocation[1])
    print(4)
    '''dest = vLot[userCoords[0]][userCoords[1]].getDestination()
    occupants += [(request.body.carColor, request.body.carType, dest)]
    vLot[userCoords[0]][userCoords[1]].setOccupantID(len(occupants) - 1)
    lotManager.setLot(vLot)
    lotManager.setOccupants(occupants)'''
    response = {
        'id': len(occupants) - 1,
        "instructions": ["Go fast3", "Turn left"],
        "exists": True
    }

    test_response = {
        'id':  7,
        "instructions": ["Go fast", "Turn left"],
        "exists": True
    }

    # return HttpResponse(response)
    return JsonResponse(response)


def requestInstructions(request):
    vLot = lotManager.getLot()
    occupants = lotManager.getOccupants()
    for y in vLot:
        for x in y:
            if x.getOccupantID() == request.body.id:
                x.setOccupantID(None)
        userCoords = [lot.getVlotCoordinates(request.body.location[0],request.body.location[1])]
        #vLot[userCoords[0]][userCoords[1]].setOccupantID(request.body.id)

        # This was broken idk why
        occupants = algorithm.main(vLot, occupants)
        
        lotManager.setOccupants(occupants)
        lotManager.setLot(vLot)
        if occupants[request.body.id].isGoing():
            response = {
                x.exists: True,
                x.text:"Move along",
                x.icon:"forward"
            }
        else:
            response = {
                x.exists: True,
                x.text:"Stop",
                x.icon:"stop"
            }
        return HttpResponse(response)


def testInstructions(request):
    response = {
        'exists': True,
        'text': "Move along",
        'icon': "forward"
    }
    return JsonResponse(response, safe=False)
