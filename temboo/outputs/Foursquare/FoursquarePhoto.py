# coding: utf-8

class FoursquarePhoto:
    """
     Contains a photo object

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

    def getHeight(self):
        """
        The height of the photo in pixels
        """
        return self.base.get("height", [])

    def getId(self):
        """
        """
        return self.base.get("id", [])

    def getPrefix(self):
        """
        The start of the URL for this photo
        """
        return self.base.get("prefix", [])

    def getSizes(self):
        return [FoursquareSize(le) for le in self.getJSONObject(self.base, "sizes").get("items", [])]


    def getSource(self):
        """
        Get the source information for this photo
        """
        return FoursquareSource(self.base.get("source", []))

    def getSuffix(self):
        """
        The end of the URL for this photo
        """
        return self.base.get("suffix", [])

    def getTip(self):
        """
        Get the tip for this photo
        """
        return FoursquareTip(self.base.get("tip", []))

    def getUrl(self):
        """
        """
        return self.base.get("url", [])

    def getUser(self):
        """
        Get the user that took this photo
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenue(self):
        """
        Get the venue associated with this photo
        """
        return FoursquareVenue(self.base.get("venue", []))

    def getVisibility(self):
        """
        """
        return self.base.get("visibility", [])

    def getWidth(self):
        """
        The width of this photo in pixels
        """
        return self.base.get("width", [])

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

from temboo.outputs.Foursquare.FoursquareSize import FoursquareSize
from temboo.outputs.Foursquare.FoursquareSource import FoursquareSource
from temboo.outputs.Foursquare.FoursquareTip import FoursquareTip
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue