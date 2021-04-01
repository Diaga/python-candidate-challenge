from django.shortcuts import render, redirect

from .models import GeoLocation, FavoritesList
from .utils import geo_reverse, geo_image_search, parse_walker


def index(request):
    """Search page"""
    longitude = request.GET.get('long', '')
    latitude = request.GET.get('lat', '')
    preset = request.GET.get('preset', '')
    page = request.GET.get('page', '0')

    geo_locations = GeoLocation.objects.all()
    params = {'banner': request.session.get('banner', ''), 'geo_locations': geo_locations, 'page': page}
    request.session['banner'] = ''

    address = None
    if longitude != '' and latitude != '':
        params['lat'] = latitude
        params['long'] = longitude

        address = geo_reverse(longitude, latitude)

    elif preset != '':
        params['preset'] = preset

        location = geo_locations.filter(id=preset).first()
        address = geo_reverse(location.longitude, location.latitude)

    if address is not None:
        params['address'] = address
        params['page'] = '1' if page == '0' else page

        walker = geo_image_search(address, page=params['page'])

        photos = parse_walker(walker, size='w')
        for photo in photos:
            photo['is_favorite'] = FavoritesList.objects.filter(
                link=photo['url']
            ).exists()

        params['photos'] = photos

    return render(request, 'index.html', params)


def geo_location(request):
    """Manage GeoLocation model page"""
    params = {'banner': request.session.get('banner', '')}

    request.session['banner'] = ''

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
    favorite_link = request.GET.get('favorite_link', None)
    title = request.GET.get('title', None)
    action = request.GET.get('action', None)

    if favorite_link is not None and title is not None:
        favorite_query = FavoritesList.objects.filter(
            link=favorite_link
        )

        if favorite_query.exists():
            favorite_query.delete()
        else:
            request.session['banner'] = 'Image added to favorite!'

            FavoritesList.objects.create(
                title=title, link=favorite_link
            )

    favorites = FavoritesList.objects.all()

    params = {'photos': favorites}

    return render(request, 'favorites.html', params)
