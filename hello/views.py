from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import algorithm
import Server.lot as lot
from django.template import loader
import algorithm
from Server.occupant import Occupant
from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


# General Notes:
# -the "request" parameter is a pull request from the client
# -you must tie each view to a url in the urls file

# index is the default or "home" webpage loaded when a client visits the url without a specified webpage
def index(request):
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
    #TODO occupants = access global server occupants array
    coord = lot.getVlotCoordinates(request.body.carLocation[0], request.body.carLocation[1])
    dest = '''globalVirtualLot'''[lot.userCoord[0]][lot.userCoord[1]].getDestination()
    lot.occupants += [Occupant(request.body.carColor, request.body.carType, dest)] #TODO find a way to access the occupant class, preferably from its own file
    response = {
        id: lot.occupants.length - 1,
        lot.instructions:["Go fast", "Turn left"]
    }
    return HttpResponse(response);
    userCoord = lot.getVlotCoordinates()

def requestInstructions(request):
    for y in '''globalVirtualLot''':
        for x in '''globalVirtualLot''':
            if (x.getOccupantID() == request.body.id):
                x.setOccupantID(None)
        coords = [lot.getVlotCoordinates(request.body.location[0],request.body.location[1])]
        '''globalVirtualLot'''[coords[0]][coords[1]].setOccupantID(request.body.id)

        # This was broken idk why
        # '''globalOccupants''' = algorithm.main('''globalVirtualLot''','''globalOccupants''')
        if ('''globalOccupants'''[request.body.id].isGoing()):
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