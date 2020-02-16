from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from analytics.models import URLObservation, UserObservation
from analytics.serializers import URLObservationSerializer, UserObservationSerializer


class ShowURLObservationView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        short_link = request.data.get('short_link', None)
        short_url = URLObservation.objects.filter(short_url__owner=request.user,
                                                  short_url__short_link=short_link).first()
        serializer = URLObservationSerializer([short_url], many=True)
        return JsonResponse(serializer.data, safe=False)


class ShowUserObservationView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        short_link = request.data.get('short_link', None)
        short_url = UserObservation.objects.filter(short_url__owner=request.user,
                                                  short_url__short_link=short_link).first()
        serializer = UserObservationSerializer([short_url], many=True)
        return JsonResponse(serializer.data, safe=False)
