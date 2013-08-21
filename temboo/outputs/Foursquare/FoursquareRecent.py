# coding: utf-8

class FoursquareRecent:
    """
     Contains recent checkins for the authenticated user
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedAt(self):
        """
        The epoch timestamp for when the checkin created
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        The checkin id
        """
        return self.base.get("id", [])

    def getPhotos(self):
        """
        Get photos for recent checkins
        """
        return [FoursquarePhoto(le) for le in self.getJSONObject(self.base, "photos").get("items", [])]


    def getSource(self):
        """
        Get the source information for this checkin
        """
        return FoursquareSource(self.base.get("source", []))

    def getTimeZone(self):
        """
        The timezone associated with this checkin
        """
        return self.base.get("timeZone", [])

    def getTimeZoneOffset(self):
        """
        String representation of the time zone where this check-in occurred
        """
        return self.base.get("timeZoneOffset", [])

    def getType(self):
        """
        The type of checkin. One of checkin, shout, or venueless.
        """
        return self.base.get("type", [])

    def getUser(self):
        """
        Get the user for this checkin
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenue(self):
        """
        Get the venue that was checked into
        """
        return FoursquareVenue(self.base.get("venue", []))

    def getBase(self):
        """
        Internal utility method; retrieve the base JSON object for this element of the response data.
        """
        return self.base

    def getJSONObject(self, json, key):
        """
        Internal utility method; retrieve a sub-object from a JSON object/array; returns an empty object if key is not present
        """
        toReturn = {}

        if json is not None:
            toReturn = json.get(key, {})

        return toReturn

from temboo.outputs.Foursquare.FoursquarePhoto import FoursquarePhoto
from temboo.outputs.Foursquare.FoursquareSource import FoursquareSource
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue