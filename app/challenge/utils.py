import os

from geopy.geocoders import Nominatim
import flickr_api as f_api

loc = Nominatim(user_agent="Flickr Photos")
f_api.set_keys(api_key=os.environ['FLICKR_API_KEY'],
               api_secret=os.environ['FLICKR_SECRET'],)


def geo_reverse(longitude, latitude):
    """Returns human readable address from geo points.
    :param: longitude: Longitude point
            latitude: Latitude point"""
    address = str(loc.reverse(f'{longitude}, {latitude}', timeout=None))
    return ', '.join(address.split(',')[-2:])


def geo_image_search(address, page=1, per_page=10):
    """Returns an iterator of Photos found on Flickr based on address
    :param: address: Human readable address"""
    walker = f_api.Walker(f_api.Photo.search, text=address, page=page, per_page=per_page)
    return walker


def parse_walker(walker, size='t', per_page=10):
    photos = []

    counter = 0
    for photo in walker:
        photos.append({
            'url': build_flickr_url(photo, size),
            'title': photo.title
        })

        counter += 1
        if counter == per_page:
            break

    return photos


def build_flickr_url(photo, size):
    """Return url using photo
    :param: photo: Flickr API Photo object
    :param: size: Size label"""
    url = f'https://live.staticflickr.com/{photo.server}/{photo.id}_{photo.secret}_{size}.jpg'
    return url
