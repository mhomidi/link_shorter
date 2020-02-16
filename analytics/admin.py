from django.contrib import admin

# Register your models here.
from analytics.models import URLObservation, UserObservation

admin.site.register(URLObservation)
admin.site.register(UserObservation)