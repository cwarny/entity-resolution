# coding: utf-8

class FoursquareComment:
    """
     A list of comments objects

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedAt(self):
        """
        """
        return self.base.get("createdAt", [])

    def getId(self):
        """
        """
        return self.base.get("id", [])

    def getText(self):
        """
        """
        return self.base.get("text", [])

    def getUser(self):
        """
        Get the user that left this comment
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