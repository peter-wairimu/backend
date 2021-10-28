from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# @api_view(['APIView'])
# @permission_classes((permissions.AllowAny,))
# def my_view(request):
    
#     content ={
#         'wmsg':'Welcome to Flashcards web app'

        
#     }
#     return Response(content)

    
class IndexView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,format=None):
    
        content ={
            'peter':'Welcome to Flashcards web app'

            
        }
        return Response(content)



