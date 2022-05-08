from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from controlapp.models import Switches

@api_view(['GET'])
def getData(request, user):
    value = Switches.objects.get(username=user)
    # value = Switches.objects.all()
    serializer = ItemSerializer(value)
    return Response(serializer.data)


@api_view(['POST'])
def putData(request, user):

    switch_object = Switches.objects.get(username=user)
    data = request.data
    # serializer = ItemSerializer(data=request.data)
    # if serializer.is_valid():
    switch_object.switch_1 = data['switch_1']
    switch_object.switch_2 = data['switch_2']
    switch_object.switch_3 = data['switch_3']
    switch_object.switch_4 = data['switch_4']
    switch_object.switch_5 = data['switch_5']
    switch_object.switch_6 = data['switch_6']
    switch_object.save()
    serializer = ItemSerializer(switch_object)
    return Response(serializer.data)
    


