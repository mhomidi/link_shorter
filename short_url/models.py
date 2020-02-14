from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from LinkShorter.settings import SITE_URL


class ShortURL(models.Model):
    main_link = models.CharField('Main URL', max_length=1000)
    short_link = models.CharField('Short URL', max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')

    @property
    def short_url(self):
        return SITE_URL + self.short_link
