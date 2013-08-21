# coding: utf-8

class FoursquareHereNowItem:
    """

        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedAt(self):
        """
        When the checkin was created in epoch format
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        The id of the checkin
        """
        return self.base.get("id", [])

    def getIsMayor(self):
        """
        Whether or not this checkin is from the mayor
        """
        return self.base.get("isMayor", [])

    def getTimeZone(self):
        """
        The timezone associated with the checkin
        """
        return self.base.get("timeZone", [])

    def getTimeZoneOffset(self):
        """
        The timezone offset associated with the checkin
        """
        return self.base.get("timeZoneOffset", [])

    def getType(self):
        """
        The type of checkin
        """
        return self.base.get("type", [])

    def getUser(self):
        """
        Get the user details
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