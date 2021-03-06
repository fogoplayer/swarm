'''
This must be executed from fogoplayer.github.io/swarm so jQuery works properly

$.getJSON('https://swarm-edd.herokuapp.com/signup', {
            carColor: "Blue",
            carType: "Sedan",
            carOrientation: "backwards",
            carLat:42.3461949,
            carLon: 83.4919403,
        }, function(data) {
            console.log(data.instructions);
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
    print("\n\n\n\n---------------Started signup view---------------------\n\n")
    occupants = lotManager.getOccupants()
    print("\ngot occupants\n")
    vLot = lotManager.getLot()
    print("\ngot vlot\n")
    print(request)
    print("vlot: " + str(vLot))
    print("lat: " + request.GET.get("carLat"))
    print("lon: " + request.GET.get("carLon"))
    userCoords = lot.getVlotCoordinates(float(request.GET.get("carLat")), float(request.GET.get("carLon")))
    print("userCoords done!")
    dest = vLot[userCoords[0]][userCoords[1]].getParent()
    print("dest done")
    occupants += [(request.GET.get("carColor"), request.GET.get("carType"), dest)]
    print("occupants done")
    lotManager.getOccupants()[userCoords[0], userCoords[1]].setOccupantID(len(occupants) - 1)
    print("vlot updated")
    lotManager.setLot(vLot)
    print("lot is set")
    lotManager.setOccupants(occupants)
    print("occupants are set")

    response = {
        'id': len(occupants) - 1,
        "instructions": ["Go fast2", "Turn left", str(request), str(type(request.GET.get("carLat")))],
        "exists": True
    }

    return JsonResponse(response, safe=False)


def requestInstructions(request):
    vLot = lotManager.getLot()
    occupants = lotManager.getOccupants()
    for y in vLot:
        for x in y:
            if x.getOccupantID() == request.GET.get("id"):
                x.setOccupantID(None)
        userCoords = [lot.getVlotCoordinates(request.GET.get("carLat"), request.GET.get("carLon"))]
        # vLot[userCoords[0]][userCoords[1]].setOccupantID(request.GET.get("id"))

        # This was broken idk why
        occupants = algorithm.main(vLot, occupants)
        
        lotManager.setOccupants(occupants)
        lotManager.setLot(vLot)
        if occupants[request.GET.get("id")].isGoing():
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
