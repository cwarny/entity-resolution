# coding: utf-8

class FacebookPlace:
    """
     An object containing information about the Facebook Page that represents the location

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getId(self):
        """
        The id of the place
        """
        return self.base.get("id", [])

    def getLocation(self):
        """
        Get location information for this place
        """
        return FacebookLocation(self.base.get("location", []))

    def getName(self):
        """
        The name of the place that was checked into
        """
        return self.base.get("name", [])

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

from temboo.outputs.Facebook.FacebookLocation import FacebookLocation