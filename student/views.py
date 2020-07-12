
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        return Response("hello",status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response("hello from POST",status=status.HTTP_200_OK)
    



@api_view(['GET','PUT', 'DELETE'])
def student_detail(request, uuid):
    uuid = uuid
    return Response(uuid, status = status.HTTP_200_OK)


