


from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .serializers import *

@api_view(['GET', 'POST'])
def hello(request):    
   data = request.data
   print('data=', data)
   return Response({"message" : "Hello world!"})
