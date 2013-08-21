# coding: utf-8

class FacebookComment:
    """
     An object representing a comment on a graph object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanRemove(self):
        """
        Whether or not the comment can be removed
        """
        return self.base.get("can_remove", [])

    def getCreatedTime(self):
        """
        The date and time that the comment was created in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that created the comment
        """
        return FacebookFrom(self.base.get("from", []))

    def getId(self):
        """
        The id of the comment
        """
        return self.base.get("id", [])

    def getLikeCount(self):
        """
        The number of times this comment was liked
        """
        return self.base.get("like_count", [])

    def getMessage(self):
        """
        The comment text
        """
        return self.base.get("message", [])

    def getUserLikes(self):
        """
        Whether or not the authenticated user likes this comment
        """
        return self.base.get("user_likes", [])

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