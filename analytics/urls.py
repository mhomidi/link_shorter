from django.urls import path

from analytics.views import *

urlpatterns = [
    path('url_observation/', ShowURLObservationView.as_view()),
    path('user_observation/', ShowUserObservationView.as_view()),
]