# coding: utf-8

class FoursquareInsight:
    """
     Contains information about insights related to this checkin
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getImage(self):
        """
        The url for the appropriate foursquare icon
        """
        return self.base.get("image", [])

    def getPoints(self):
        """
        Get the points information for the insight
        """
        return FoursquarePoints(self.base.get("points", []))

    def getTitle(self):
        """
        The title of the insight
        """
        return self.base.get("title", [])

    def getType(self):
        """
        The type of insight
        """
        return self.base.get("type", [])

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

from temboo.outputs.Foursquare.FoursquarePoints import FoursquarePoints