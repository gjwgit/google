import os
import sys

from geocode import geocode
from mlhub.pkg import mlask, mlcat, get_private


mlcat("Google Maps", """\
Welcome to Google Maps REST service. This service can identify the latitude
and longitude coordinates that correspond to the supplied location/address
information.
""")

mlask(end="\n")

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

key = get_private()[0]


mlcat("GEOCODE", """\
Here's an example. We provide the location

    Albany Creek


and Google will attempt to match this using its extensive map data.
The result includes the logitude, latitude, and neighbourhood bounding
box, how good the match is, the type of the location, and a clean
address.
""")

mlask(end="\n")

# ----------------------------------------------------------------------
# If the google maps key is not correct, the user needs to run
# ml configure google to update key
# ----------------------------------------------------------------------
try:
    location = geocode("Albany Creek", key, "5", False)

except Exception as e:
    sys.exit(f"The google maps key is not correct: {e}\n" +
          "Please run ml configure google to update your key.",)

location = location[0]
out = location.split(",")
latlong = out[0].split(":")
bbox = out[1]

print(f"Latitude:  {latlong[0]}\nLongitude: {latlong[1]}\n")
print(f"Bounding Box: {out[1]}\n")
print(f"Confidence: {out[2]}; Code: {out[3]}\n\nType: {out[4]}\n")
print(f"Address: {','.join(out[5:])}")
print("")

mlcat("NEXT", """\
You can use the 'geocode' command to obtain this output for yourself.

      $ ml geocode google Priceline Pharmacy Albany Creek
""")
