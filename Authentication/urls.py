from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from Authentication.views import *

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
]