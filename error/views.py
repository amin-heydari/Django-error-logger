from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def error_view(request):
    raise Exception("this is the error")


class APIErrorView(APIView):
    def post(self, request, format=None):
        raise Exception("This is a DRF API view error.")
