# coding: utf-8

class FoursquareBadge:
    """
     Contains badges associated with the checkin

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBadgeId(self):
        """
        A canonical ID for this badge
        """
        return self.base.get("badgeId", [])

    def getDescription(self):
        """
        The badge description
        """
        return self.base.get("description", [])

    def getId(self):
        """
        A unique identifier for this badge
        """
        return self.base.get("id", [])

    def getBadgeImage(self):
        """
        Get the badge image information
        """
        return FoursquareBadgeImage(self.base.get("image", []))

    def getName(self):
        """
        The name of the badge
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

from temboo.outputs.Foursquare.FoursquareBadgeImage import FoursquareBadgeImage