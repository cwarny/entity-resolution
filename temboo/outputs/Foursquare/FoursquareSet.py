# coding: utf-8

class FoursquareSet:
    """
     Contains badge IDs and badge image information
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBadgeImage(self):
        """
        Get badge image info
        """
        return FoursquareBadgeImage(self.base.get("image", []))

    def getBadgeIDs(self):
        """
        Contains badge ids
        """
        return [le for le in self.base.get("items", [])]


    def getName(self):
        """
        The name of the badge
        """
        return self.base.get("name", [])

    def getType(self):
        """
        The badge type
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

from temboo.outputs.Foursquare.FoursquareBadgeImage import FoursquareBadgeImage