from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
from pip._vendor import requests
from rest_framework.views import APIView

from Authentication.utils import my_validate_email
from LinkShorter.settings import SITE_URL


class Login(APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = User.objects.filter(email=username).first() or User.objects.filter(username=username).first()
        if user is not None:
            return HttpResponse(requests.post(SITE_URL + 'auth/token/',
                            json={
                                "username": user.username,
                                "password": password
                            }
                            ), content_type='application/json')
        return HttpResponse(requests.post(SITE_URL + 'auth/token/',
                                          json={
                                              "username": username,
                                              "password": password
                                          }
                                          ), content_type='application/json')


class Register(APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        email = request.data.get('email', None)
        if username and email and password and my_validate_email(email):
            User.objects.create_user(username, email, password)
            return HttpResponse(requests.post(SITE_URL + 'auth/token/',
                                              json={
                                                  "username": username,
                                                  "password": password
                                              }
                                              ), content_type='application/json')
        return HttpResponse("{\"err\": \"Bad input\"}", status=400)