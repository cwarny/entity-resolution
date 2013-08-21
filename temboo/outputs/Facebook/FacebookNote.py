# coding: utf-8

class FacebookNote:
    """
     An object containing information about the authenticated user's note

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedTime(self):
        """
        The date and time the note was created
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that the note is from
        """
        return FacebookFrom(self.base.get("from", []))

    def getIcon(self):
        """
        The icon for the note
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the note
        """
        return self.base.get("id", [])

    def getMessage(self):
        """
        The message
        """
        return self.base.get("message", [])

    def getSubject(self):
        """
        The subject of the note
        """
        return self.base.get("subject", [])

    def getUpdatedTime(self):
        """
        The last updated time of the note
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

from temboo.outputs.Facebook.FacebookFrom import FacebookFrom