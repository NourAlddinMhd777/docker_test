from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status

@api_view(["GET"])
def fun_view(request):

    return Response("hello world2!",status=200)

