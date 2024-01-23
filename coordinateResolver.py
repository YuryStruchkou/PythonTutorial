from geopy.geocoders import Nominatim


def resolve(latitude: float, longitude: float) -> dict[str, object]:
    user_agent = 'test-coordinate-resolver'
    geolocator = Nominatim(user_agent=user_agent)
    location = geolocator.reverse(f'{latitude}, {longitude}', language='en')
    return location.raw
