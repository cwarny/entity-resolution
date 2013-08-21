# coding: utf-8

class FoursquareHereNowList:
    """
     Contains a count and list of people at this venue right now
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        The total number of people here now
        """
        return self.base.get("count", [])

    def getHereNowItems(self):
        """
        Get checkins and user info for people here now
        """
        return [FoursquareHereNowItem(le) for le in self.base.get("items", [])]


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

from temboo.outputs.Foursquare.FoursquareHereNowItem import FoursquareHereNowItem