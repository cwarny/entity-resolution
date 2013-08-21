# coding: utf-8

class FoursquareTip:
    """
     Contains information about tips associated with a venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanonicalUrl(self):
        """
        The url for the tip
        """
        return self.base.get("canonicalUrl", [])

    def getCreatedAt(self):
        """
        The date that this tip was created in epoch format
        """
        return self.base.get("createdAt", [])

    def getDone(self):
        """
        Get the count of tips that have been done
        """
        return FoursquareDone(self.base.get("done", []))

    def getId(self):
        """
        The id of the tip
        """
        return self.base.get("id", [])

    def getPhoto(self):
        """
        Get the photos for this tip
        """
        return FoursquarePhoto(self.getJSONObject(self.base, "items").get("photo", []))

    def getLikes(self):
        """
        Get the likes for this tip
        """
        return FoursquareLikes(self.base.get("likes", []))

    def getPhotourl(self):
        """
        The url to the photo
        """
        return self.base.get("photourl", [])

    def getText(self):
        """
        The text of the tip
        """
        return self.base.get("text", [])

    def getTodo(self):
        """
        Get to count of todos for this tip
        """
        return FoursquareTodo(self.base.get("todo", []))

    def getUrl(self):
        """
        The tip url
        """
        return self.base.get("url", [])

    def getUser(self):
        """
        Get the user that created this tip
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

from temboo.outputs.Foursquare.FoursquareDone import FoursquareDone
from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquarePhoto import FoursquarePhoto
from temboo.outputs.Foursquare.FoursquareTodo import FoursquareTodo
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser