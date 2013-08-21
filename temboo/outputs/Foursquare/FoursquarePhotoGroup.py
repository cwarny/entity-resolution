# coding: utf-8

class FoursquarePhotoGroup:
    """
     Contains checkin photos and venue photos

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        """
        return self.base.get("count", [])

    def getPhotos(self):
        """
        Get a photo associated with the venue
        """
        return [FoursquarePhoto(le) for le in self.base.get("items", [])]


    def getName(self):
        """
        The name of the photo group
        """
        return self.base.get("name", [])

    def getType(self):
        """
        The photo group type
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

from temboo.outputs.Foursquare.FoursquarePhoto import FoursquarePhoto