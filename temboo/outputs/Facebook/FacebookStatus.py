# coding: utf-8

class FacebookStatus:
    """
     A status messages on a user's wall

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getComments(self):
        """
        Get the comments for this status
        """
        return [FacebookComment(le) for le in self.getJSONObject(self.base, "comments").get("data", [])]


    def getFrom(self):
        """
        Get the user that posted this status
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

    def getUpdatedTime(self):
        """
        The time the message was published in ISO-8601 format
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