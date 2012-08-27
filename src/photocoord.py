#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
using: python photocoord.py filename
"""

import sys
import urllib

import EXIF


def getGpsCoord (fname):
    """
    fname - filename with photo
    Return tuple: (latitude, longitude). Latitude and longitude returns in degrees
    If fname fot exits then raise IOError exception
    """
    with open (fname) as fp:
        tags = EXIF.process_file (fp, strict=True)

    latitude = calcToDegrees (tags["GPS GPSLatitude"])
    longitude = calcToDegrees (tags["GPS GPSLongitude"])

    return (latitude, longitude)


def getYandexLink (latitude, longitude):
    """
    Return link to http://maps.yandex.ru for coordinates
    """
    request = "{latitude} N, {longitude} E".format (latitude=latitude, longitude=longitude)
    request = urllib.quote (request)

    link = "http://maps.yandex.ru/?text={0}".format (request)
    return link


def getGoogleLink (latitude, longitude):
    """
    Return link to http://maps.google.ru for coordinates
    """
    request = "{latitude}+N,+{longitude}+E".format (latitude=latitude, longitude=longitude)

    link = "http://maps.google.ru/?q={0}".format (request)
    return link


def getWikimapiaLink (latitude, longitude):
    """
    Return link to http://wikimapia.org for coordinates
    """
    request = "{latitude} N, {longitude} E".format (latitude=latitude, longitude=longitude)
    request = urllib.quote (request)

    link = "http://wikimapia.org/#lat={latitude}&lon={longitude}&search={request}".format (latitude=latitude, longitude=longitude, request=request)
    return link


def getOSMLink (latitude, longitude):
    """
    Return link to http://www.openstreetmap.org/ for coordinates
    """
    link = "http://www.openstreetmap.org/?mlat={latitude}&mlon={longitude}zoom=10&layers=M".format (latitude=latitude, longitude=longitude)

    return link


def calcToDegrees (gpsdata):
    """
    gpsdata - instance of EXIF.Ratio
    Return result in degrees
    """
    degrees = float (gpsdata.values[0].num) / gpsdata.values[0].den
    minutes = float (gpsdata.values[1].num) / gpsdata.values[1].den
    seconds = float (gpsdata.values[2].num) / gpsdata.values[2].den

    return degrees + minutes / 60.0 + seconds / 3600.0


if __name__ == "__main__":
    if len (sys.argv) < 2:
        print "using: python photocoord.py filename"
        sys.exit (1)

    fname = sys.argv[1]
    try:
        (latitude, longitude) = getGpsCoord (fname)
    except IOError:
        print "Can't open file '{0}'".format (fname)
        sys.exit (1)
    except KeyError:
        print "GPS data not found in '{0}'".format (fname)
        sys.exit (1)

    print getYandexLink (latitude, longitude)
    print getGoogleLink (latitude, longitude)
    print getWikimapiaLink (latitude, longitude)
    print getOSMLink (latitude, longitude)
