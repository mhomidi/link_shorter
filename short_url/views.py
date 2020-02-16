from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from LinkShorter import settings
from analytics.utils import record_observations
from short_url.models import ShortURL
from short_url.serializers import ShortURLSerializer
from short_url.utils import create_short_link



class ShowLinkView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        main_link = request.data.get('main_link', None)
        short_url = ShortURL.objects.filter(main_link=main_link, owner=request.user)
        serializer = ShortURLSerializer(short_url, many=True)
        return JsonResponse(serializer.data, safe=False)


class CreateShortLinkView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request):
        main_link = request.data.get('main_link', None)
        short_link = request.data.get('short_link', None)
        link_created = create_short_link(main_link=main_link, short_link=short_link, user=request.user)
        if link_created:
            return JsonResponse({'status': 200, 'text': 'Your link created successfully'}, safe=False)
        return JsonResponse({'status': 400, 'text': 'You short link exists or not be alphanumeric' +
                                                    ' or your main_link is corrupted'}, safe=False)


class Redirect(APIView):

    def get(self, request, short_link):
        record_observations(request, short_link)
        short_url = get_object_or_404(ShortURL, short_link=short_link)
        # return JsonResponse({'status': 200, 'text': 'You redirect successfully'}, safe=False)  # for redis test
        return redirect(short_url.main_link)