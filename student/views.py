
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from . import libs as student_libs
# Create your views here.


@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        response = student_libs.get_students()
        return Response(response,status=status.HTTP_200_OK)
    if request.method == 'POST':
        return Response("hello from POST",status=status.HTTP_200_OK)
    



@api_view(['GET','PUT', 'DELETE'])
def student_detail(request, uuid):
    uuid = uuid
    if request.method == 'GET':
        response = student_libs.get_student_by_uuid(uuid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        response = student_libs.delete_student(uuid)
    
    return Response(uuid, status = status.HTTP_200_OK)


