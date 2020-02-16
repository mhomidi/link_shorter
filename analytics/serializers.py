from rest_framework import serializers

from analytics.models import URLObservation, UserObservation


class URLObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = URLObservation
        fields = ['chrome', 'mozilla', 'safari', 'ie', 'opera', 'other_browser']


class UserObservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserObservation
        fields = ['chrome', 'mozilla', 'safari', 'ie', 'opera', 'other_browser']