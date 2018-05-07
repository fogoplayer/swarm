from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import algorithm
import Server.lot as lot
from django.template import loader
import algorithm
from Server.occupant import Occupant
from .models import Greeting
import manager as lotManager

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
    occupants = lotManager.getOccupants()
    vLot = lotManager.getLot()
    userCoords = lot.getVlotCoordinates(request.body.carLocation[0], request.body.carLocation[1])
    dest = vLot[userCoords[0]][lot.userCoords[1]].getDestination()
    occupants += [Occupant(request.body.carColor, request.body.carType, dest)] #TODO find a way to access the occupant class, preferably from its own file
    vLot[userCoord[0]][lot.userCoord[1]].setOccupantID(occupants.length - 1);
    lotManager.setLot(vLot)
    lotManager.setOccupants(occupants)
    
    response = {
        id: lot.occupants.length - 1,
        lot.instructions:["Go fast", "Turn left"]
    }
    return HttpResponse(response);


def requestInstructions(request):
    vLot = lotManager.getLot()
    occupants = lotManager.getOccupants()
    for y in vLot:
        for x in y:
            if x.getOccupantID() == request.body.id:
                x.setOccupantID(None)
        userCoords = [lot.getVlotCoordinates(request.body.location[0],request.body.location[1])]
        vLot[userCoords[0]][userCoords[1]].setOccupantID(request.body.id)

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
