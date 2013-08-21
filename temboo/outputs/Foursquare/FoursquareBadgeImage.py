# coding: utf-8

class FoursquareBadgeImage:
    """
     Contains the image information for badges
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getName(self):
        """
        """
        return self.base.get("name", [])

    def getPrefix(self):
        """
        """
        return self.base.get("prefix", [])

    def getSizes(self):
        """
        """
        return [le for le in self.base.get("sizes", [])]


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

