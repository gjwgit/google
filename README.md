# Google Maps 

This [MLHub](https://mlhub.ai) package provides a demonstration and
command line tools built from Google Maps REST service. This service
can generate a list of coordinates (latitude and longitude) based on
the provided location.

A Google Maps Key is required.

**Warning** Unlike the MLHub models in general these Google Map REST
services use *closed source services* which have no guarantee of
ongoing availability and do not come with the freedom to modify and
share.

## Quick Start

```console
$ ml geocode google back creek
$ ml geocode google back creek --max=1
$ ml geocode google back creek --url
$ ml geocode google back creek --google
$ ml geocode google back creek --google
$ brave-browser `ml geocode google --max=1 --url albany creek`
```

## Usage

- To install mlhub (Ubuntu):

		$ pip3 install mlhub
		$ ml configure

- To install, configure, and run the demo:

		$ ml install   google
		$ ml configure google
		$ ml readme    google
		$ ml commands  google
		$ ml demo      google
		
- Command line tools:

		$ ml geocode google [options] <address>
		       -b            --bing               Generate Bing Maps URL.
			 -g            --google             Generate Google Maps URL.
			 -m <int>      --max=<int> 	    Maximum number of matches.
			 -o            --osm                Generate Open Street Map URL.
			 -u            --url                Generate Open Street Map URL.
			 -n            --neighborhood       Include the neighborhood when it is available.

## Command Line Tools

In addition to the *demo* command below, the package provides a number
of useful command line tools.

### *geocode*

The *geocode* command will generate a list of coordinate pairs for the provided
location. Each coordinate pair includes latitude and longitude. If the provided
location is specific, the result will be a list with one element. If the location
is ambiguous, such as a duplicate name in Australia, a list with several elements 
will be shown. It has the option to specify the maximum number of coordinates to 
return in the response. The number is between 1-20, and the default is 5. Also,
this service provides the option to include the neighborhood with the address
information when it is available. The default is 0 (Do not include neighborhood
information). We provide --google --bing and --osm option to show the location 
in the Google Map, Bing Map and Open street Map.

Not every location has neighborhood, the system will print available neighborhood if --inclnb 
is 1. 

```console
$ ml geocode google PriceLine Pharmacy Albany Creek

$ ml geocode google back creek --max=3
$ ml geocode google back creek --inclnb

$ brave-browser `ml geocode google --max=1 --osm albany creek`

$ brave-browser `ml geocode google bunnings mentone 23-27 nepean hwy mentone vic 3194 --osm`

```

```console
$ ml geocode google  Ballard, WA

47.669593811035156:-122.38619995117188,47.659759521484375:-122.39840698242188:47.67599868774414:-122.3759994506836,High,Ambiguous,Neighborhood,Ballard, WA, United States
47.675296783447266:-122.38217163085938,47.656524658203125:-122.4110336303711:47.697792053222656:-122.36068725585938,Medium,Ambiguous,Neighborhood,Ballard, WA, United States
```
For each line, the first element is coordinates, the second element is bounding
box, the thirdis confidence, fourth is match code, fifth is entity Type and the 
sixth is address.

## Demonstration
```console

=======
GEOCODE
=======

Here's an example. We provide the location

    Priceline Pharmacy Albany Creek

 and Google will attempt to match this using its extensive map data. The
result includes the logitude, latitude, and neighbourhood bounding
box, how good the match is, the type of the location, and a clean
address.

Press Enter to continue: 

Latitude:  -27.35361099243164
Longitude: 152.96832275390625

Bounding Box: -27.372652053833008:152.94793701171875:-27.334684371948242:152.98854064941406

Confidence: Medium; Code: UpHierarchy

Type: PopulatedPlace

Address: Albany Creek, QLD, Australia

====
NEXT
====

You can use the 'geocode' command to obtain this output for yourself.

      $ ml geocode google Priceline Pharmacy Albany Creek


```
