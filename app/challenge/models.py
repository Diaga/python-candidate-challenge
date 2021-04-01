from django.db import models

from uuid import uuid4


class GeoLocation(models.Model):
    """Preset list storing location (long, lat)
    with a human readable name"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        app_label = 'challenge'
        default_related_name = 'geo_locations'

    def __str__(self):
        return f'{self.name} - ({self.latitude}, {self.longitude})'


class FavoritesList(models.Model):
    """Stores a search result list"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.TextField()
    link = models.TextField()

    class Meta:
        app_label = 'challenge'
        default_related_name = 'favorites_lists'

    def __str__(self):
        return f'{self.title} - {self.link}'
