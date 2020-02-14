from django.contrib import admin

# Register your models here.
from short_url.models import ShortURL

admin.site.register(ShortURL)