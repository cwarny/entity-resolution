# coding: utf-8

class FoursquareSpecialsList:
    """
     Contains a list of specials
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDescription(self):
        """
        The special description
        """
        return self.base.get("description", [])

    def getFinePrint(self):
        """
        The fine print of the special
        """
        return self.base.get("finePrint", [])

    def getIcon(self):
        """
        The icon name
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The special id
        """
        return self.base.get("id", [])

    def getLikes(self):
        """
        Get the likes for the special
        """
        return FoursquareLikes(self.base.get("likes", []))

    def getMessage(self):
        """
        The message text for this special
        """
        return self.base.get("message", [])

    def getProvider(self):
        """
        The provider of the special
        """
        return self.base.get("provider", [])

    def getRedemption(self):
        """
        The redemption type
        """
        return self.base.get("redemption", [])

    def getTitle(self):
        """
        The title of the special
        """
        return self.base.get("title", [])

    def getType(self):
        """
        The special type
        """
        return self.base.get("type", [])

    def getVenue(self):
        """
        Get the venue offering the special
        """
        return FoursquareVenue(self.base.get("venue", []))

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

from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue