# coding: utf-8

class FoursquareTipDetails:
    """
     Contains tip details including users that have marked a tip done and users that have marked a tip as a todo

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
        An epoch timestamp when the tip was created
        """
        return self.base.get("createdAt", [])

    def getDone(self):
        """
        Get the info for user who have marked this tip done
        """
        return FoursquareDone(self.base.get("done", []))

    def getId(self):
        """
        The id of this tip
        """
        return self.base.get("id", [])

    def getLike(self):
        """
        Whether or not the tip has been liked
        """
        return self.base.get("like", [])

    def getLikes(self):
        """
        Get the likes for this tip
        """
        return FoursquareLikes(self.base.get("likes", []))

    def getListed(self):
        """
        Get the the count of tip
        """
        return FoursquareListed(self.base.get("listed", []))

    def getText(self):
        """
        The actual tip
        """
        return self.base.get("text", [])

    def getTodo(self):
        """
        Get information about people that have indicated this tip as a todo
        """
        return FoursquareTodo(self.base.get("todo", []))

    def getUser(self):
        """
        Get the user that created this tip
        """
        return FoursquareUser(self.base.get("user", []))

    def getVenue(self):
        """
        Get the venue associated with this tip
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

from temboo.outputs.Foursquare.FoursquareDone import FoursquareDone
from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquareListed import FoursquareListed
from temboo.outputs.Foursquare.FoursquareTodo import FoursquareTodo
from temboo.outputs.Foursquare.FoursquareUser import FoursquareUser
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue