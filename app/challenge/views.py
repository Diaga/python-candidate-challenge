from django.shortcuts import render, redirect

from .models import GeoLocation, FavoritesList
from .utils import geo_reverse, geo_image_search, parse_walker


def index(request):
    """Search page"""
    longitude = request.GET.get('long', None)
    latitude = request.GET.get('lat', None)
    preset = request.GET.get('preset', None)
    page = request.GET.get('page', 1)

    geo_locations = GeoLocation.objects.all()
    params = {'banner': '', 'geo_locations': geo_locations, 'page': page}

    address = None
    if longitude is not None and latitude is not None:
        params['lat'] = latitude
        params['long'] = longitude

        address = geo_reverse(longitude, latitude)

    elif preset is not None:
        params['preset'] = preset

        location = geo_locations.filter(id=preset).first()
        address = geo_reverse(location.longitude, location.latitude)

    params['address'] = address
    walker = geo_image_search(address, page=page)
    params['photos'] = parse_walker(walker, size='w')

    return render(request, 'index.html', params)


def geo_location(request):
    """Manage GeoLocation model page"""
    params = {'banner': request.session.get('banner', '')}

    if request.method == 'POST':
        name = request.POST.get('name', None)
        longitude = request.POST.get('long', None)
        latitude = request.POST.get('lat', None)

        GeoLocation.objects.create(
            name=name, longitude=longitude, latitude=latitude
        )

        params['banner'] = 'Preset added to list successfully!'

    geo_locations = GeoLocation.objects.all()
    params['geo_locations'] = geo_locations

    return render(request, 'geo_location.html', params)


def geo_location_delete(request, location_id):
    """Delete geo location using location id"""

    location = GeoLocation.objects.filter(id=location_id)

    if location.exists():
        location.delete()

        request.session['banner'] = 'Geo Location deleted successfully!'
    else:
        request.session['banner'] = 'Geo Location does not exist!'

    return redirect('geo_location')


def geo_location_favorites(request):
    """Return favorite images"""
    pass
