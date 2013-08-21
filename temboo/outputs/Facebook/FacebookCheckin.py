# coding: utf-8

class FacebookCheckin:
    """
     A Checkin object represents a single visit to a location

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getApplication(self):
        """
        The application that created this checkin
        """
        return FacebookApplication(self.base.get("application", []))

    def getComments(self):
        """
        Get the comments for this checkin
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getCreatedTime(self):
        """
        The date and time the checkin was created in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that the checkin is from
        """
        return FacebookFrom(self.base.get("from", []))

    def getId(self):
        """
        The id of the checkin
        """
        return self.base.get("id", [])

    def getLikes(self):
        """
        Get likes for this checkin
        """
        return [FacebookLike(le) for le in self.getJSONObject(self.base, "likes").get("data", [])]


    def getPlace(self):
        """
        Get the place and location for this checkin
        """
        return FacebookPlace(self.base.get("place", []))

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

from temboo.outputs.Facebook.FacebookApplication import FacebookApplication
from temboo.outputs.Facebook.FacebookComment import FacebookComment
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookLike import FacebookLike
from temboo.outputs.Facebook.FacebookPlace import FacebookPlace