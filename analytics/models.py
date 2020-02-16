import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from short_url.models import ShortURL


class Observation(models.Model):
    MOBILE = 0
    DESKTOP = 1
    DEVICE_CHOICE  = (
        (MOBILE, 'Mobile'),
        (DESKTOP, 'Desktop'),
    )

    CHROME = 0
    MOZILA = 1
    SAFARI = 2
    IE = 3
    OPERA = 4
    OTHERS = 5
    BROWSER_CHOICE = (
        (CHROME, 'Chrome'),
        (MOZILA, 'Mozilla'),
        (SAFARI, 'Safari'),
        (IE, 'IE'),
        (OPERA, 'Opera'),
        (OTHERS, 'Others')
    )

    device = models.IntegerField('Device', choices=DEVICE_CHOICE, default=0)
    browser = models.IntegerField('Browser', choices=BROWSER_CHOICE, default=0)
    create_date = models.DateField('Create Date', default=datetime.date.today())

    @property
    def device_type(self):
        return self.DEVICE_CHOICE[self.device][1]

    @property
    def browser_type(self):
        return self.BROWSER_CHOICE[self.browser][1]


class URLObservation(Observation):

    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE, null=True, default=None)

    @property
    def chrome(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.CHROME).count()

    @property
    def mozilla(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.MOZILA).count()

    @property
    def safari(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.SAFARI).count()

    @property
    def ie(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.IE).count()

    @property
    def opera(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.OPERA).count()

    @property
    def other_browser(self):
        return URLObservation.objects.filter(short_url=self.short_url, browser=self.IE).count()


class UserObservation(Observation):
    owner_ip = models.CharField('Owner IP', max_length=20, default='127.0.0.1')
    short_url = models.ForeignKey(ShortURL, on_delete=models.CASCADE, null=True, default=None)

    @property
    def chrome(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.CHROME).count()

    @property
    def mozilla(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.MOZILA).count()

    @property
    def safari(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.SAFARI).count()

    @property
    def ie(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.IE).count()

    @property
    def opera(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.OPERA).count()

    @property
    def other_browser(self):
        return UserObservation.objects.filter(short_url=self.short_url, browser=self.IE).count()
