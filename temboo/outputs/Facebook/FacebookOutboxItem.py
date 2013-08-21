# coding: utf-8

class FacebookOutboxItem:
    """
     An object containing information for an outbox message

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getComments(self):
        """
        The comments for this outbox item
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getFrom(self):
        """
        Get the user that the outbox item has been sent from
        """
        return FacebookFrom(self.base.get("from", []))

    def getId(self):
        """
        The id of the message
        """
        return self.base.get("id", [])

    def getMessage(self):
        """
        The message text
        """
        return self.base.get("message", [])

    def getTo(self):
        """
        Get the user that the message has been sent to
        """
        return [FacebookTo(le) for le in self.getJSONObject(self.base, "to").get("data", [])]


    def getUnread(self):
        """
        Number of unread messages in the thread
        """
        return self.base.get("unread", [])

    def getUnseen(self):
        """
        Whether or not the there are unseen messages
        """
        return self.base.get("unseen", [])

    def getUpdatedTime(self):
        """
        Timestamp of when the thread was last updated
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
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookTo import FacebookTo