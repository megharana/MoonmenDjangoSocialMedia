from django.shortcuts import render
from socialAuth.forms import createUser_form

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



def home(request):
	return render(request, 'home.html')


def login(request):
	return render(request, 'login.html')


@api_view(['GET', 'POST', ])
def oauthLogin(request):
	try:
		print(str(request.body))

		return Response(status.HTTP_201_CREATED)
	except ValueError as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)