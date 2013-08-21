# coding: utf-8

class FoursquarePoints:
    """
     Contains information for points for the insight
          
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getImage(self):
        return FoursquareImage(self.base.get("image", []))

    def getMessage(self):
        """
        A foursquare generated message about the checkin
        """
        return self.base.get("message", [])

    def getPoints(self):
        """
        The number of points
        """
        return self.base.get("points", [])

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

from temboo.outputs.Foursquare.FoursquareImage import FoursquareImage