from rest_framework import serializers

from short_url.models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortURL
        fields = ['main_link', 'short_url']
