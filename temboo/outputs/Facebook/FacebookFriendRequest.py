# coding: utf-8

class FacebookFriendRequest:
    """
     An object containing information about the friend request

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedTime(self):
        """
        The date and time of the friend request
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that the friend request is from
        """
        return FacebookFrom(self.base.get("from", []))

    def getTo(self):
        """
        Get the user that the friend request was sent to
        """
        return FacebookTo(self.base.get("to", []))

    def getUnread(self):
        """
        Whether or not the friend request has been read
        """
        return self.base.get("unread", [])

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

from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookTo import FacebookTo