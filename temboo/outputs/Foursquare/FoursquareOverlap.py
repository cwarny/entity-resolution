# coding: utf-8

class FoursquareOverlap:
    """
     Contains information about overlapping checkins
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedAt(self):
        """
        The epoch timestamp for the overlapping checkin
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        The id of the overlapping ehckin
        """
        return self.base.get("id", [])

    def getTimeZone(self):
        """
        The timezone for the overlapping checkin
        """
        return self.base.get("timeZone", [])

    def getTimeZoneOffset(self):
        """
        The timezone offset for the checkin
        """
        return self.base.get("timeZoneOffset", [])

    def getType(self):
        """
        The type of foursquare object
        """
        return self.base.get("type", [])

    def getUser(self):
        """
        Get the users overlapping with the checkin
        """
        return FoursquareUser(self.base.get("user", []))

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

from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser