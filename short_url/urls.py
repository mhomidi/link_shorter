from django.urls import path

from short_url.views import *

urlpatterns = [
    path('get_short_link/', ShowLinkView.as_view()),
    path('create/', CreateShortLinkView.as_view()),
]