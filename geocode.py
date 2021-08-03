import requests
import sys
import os
import argparse

from mlhub.pkg import get_private


def geocode(address, key, max=5, url=None):
    """Generate potential latitude and longitude coordinates.

    Arguments
    ---------

    address (str) The address to look up.

    key (str) The google maps key.

    max (int) The maximum number of matches.

    url (str) Whether to return a URL string: None, Google, Bing, OSM.

    Return
    ------

    string The matched information, comma separated:
      lat:long,bbox,confidence,type,code,address
    OR
    string A URL ready to be used within a browser.
    """

    result = []

    # Google Maps API endpoint for Australian addresses.

    API_URL = (
        "https://maps.googleapis.com/maps/api/geocode/json?"
        + f"&address={address}&components=country:AU&key={key}")

    # Get JSON response from Google Maps API.

    response = requests.get(API_URL).json()

    locations = response["results"]

    for item in locations:

        loc = ""
        
        try:
            # Get the latitude and longitude coordinates from the JSON response
            latitude = item["geometry"]["location"]["lat"]
            longitude = item["geometry"]["location"]["lng"]
            coords = f"{latitude}:{longitude}"
        except:
            raise Exception("Invalid address!")

        try:
            # Get the bounding box coordinates from the JSON response
            slat = item["geometry"]["bounds"]["southwest"]['lat']
            wlong = item["geometry"]["bounds"]["southwest"]["lng"]
            nlat = item["geometry"]["bounds"]["northeast"]["lat"]
            elong = item["geometry"]["bounds"]["northeast"]["lng"]
            bbox = f"{slat}:{wlong}:{nlat}:{elong}"
        except:
            raise Exception("Invalid address!")

        try:
            # Get the geocoded address from the JSON response
            geo_address = item["formatted_address"]
        except:
            raise Exception("Invalid address!")

        try:
            # Get the address components from the JSON response
            address_components = item["address_components"]
        except:
            raise Exception("Invalid address!")
        
        try:
            # Get the state from the JSON response
            state = ""
            for compo in address_components:
                if compo["types"][0] == "administrative_area_level_1":
                    state = compo["long_name"]
        except:
            raise Exception("Invalid address!")

        try:
            # Get the country from the JSON response
            country = ""
            for compo in address_components:
                if compo["types"][0] == "country":
                    country = compo["long_name"]
        except:
            raise Exception("Invalid address!")

        ## TODO UPDATE BING TO OUTPUT

        ## lat:long,bbox,type,country,state,address
        
        if url:
            if url == "bing":
                loc = "https://maps.bing.com/"
                loc += f"?cp={latitude}~{longitude}&lvl=18&style=r"
            elif url == "google":
                loc = "https://maps.google.com/"
                loc += f"?q={latitude},{longitude}"
            else:
                loc = "http://www.openstreetmap.org/"
                loc += f"?mlat={latitude}&mlon={longitude}&zoom=18"
        else:
            loc = f"{coords},{bbox},{type},{country},{state},{geo_address}"

        result.append(loc)

    return result


if __name__ == "__main__":

    key = get_private()[0]

    # Private file stores the Bing Maps key required by the geocoding
    # function.

    parser = argparse.ArgumentParser(description='Google Maps')

    parser.add_argument(
        'address',
        type=str,
        nargs='*',
        help='location to geocode')

    parser.add_argument(
        '--neighbourhood', '-n',
        action="store_true",
        help='include neighbourhood of the address.')

    parser.add_argument(
        '--max', '-m',
        type=int,
        default=5,
        help='maximum number of locations to return (1-20)')

    parser.add_argument(
        '--url', '-u',
        action="store_true",
        help='return map URL (Open Street Map)')

    parser.add_argument(
        '--osm', '-o',
        action="store_true",
        help='return Open Street Map map URL')

    parser.add_argument(
        '--bing', '-b',
        action="store_true",
        help='return Bing map URL')

    parser.add_argument(
        '--google', '-g',
        action="store_true",
        help='return Google map URL')

    args = parser.parse_args()

    address = " ".join(args.address)
    max = args.max
    url = "osm" if args.osm or args.url else "bing" if args.bing else \
        "google" if args.google else None

    try:
        result = geocode(address, key, max, url)
        print("\n".join(result))

    except Exception as e:
        sys.exit(f"Geocoding failed: {e}.")
