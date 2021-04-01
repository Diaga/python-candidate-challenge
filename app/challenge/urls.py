from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('geo-locations', views.geo_location, name='geo_location'),
    path('geo-locations/favorites', views.geo_location_favorites, name='geo_location_favorites'),
    path('geo-locations/delete/<uuid:location_id>', views.geo_location_delete, name='geo_location_delete')
]
