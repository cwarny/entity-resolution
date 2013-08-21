# coding: utf-8

class FacebookInboxItem:
    """
     An inbox object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getComments(self):
        """
        The comment for an inbox message
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getId(self):
        """
        The id of the inbox item
        """
        return self.base.get("id", [])

    def getTo(self):
        """
        Get the user that the message has been sent to
        """
        return [FacebookTo(le) for le in self.getJSONObject(self.base, "to").get("data", [])]


    def getUnread(self):
        """
        The number of unread comments for this inbox item
        """
        return self.base.get("unread", [])

    def getUnseen(self):
        """
        Whether or not the message has been seen yet
        """
        return self.base.get("unseen", [])

    def getUpdatedTime(self):
        """
        The last updated time for this thread
        """
        return self.base.get("updated_time", [])

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

from temboo.outputs.Facebook.FacebookComment import FacebookComment
from temboo.outputs.Facebook.FacebookTo import FacebookTo