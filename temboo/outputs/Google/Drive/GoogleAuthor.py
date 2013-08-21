# coding: utf-8

class GoogleAuthor:
    """
     An object representing the user who wrote this comment

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDisplayName(self):
        """
        A plain text displayable name for this user
        """
        return self.base.get("displayName", [])

    def getIsAuthenticatedUser(self):
        """
        Whether this user is the same as the authenticated user of which the request was made on behalf
        """
        return self.base.get("isAuthenticatedUser", [])

    def getKind(self):
        """
        This is always drive#user
        """
        return self.base.get("kind", [])

    def getPicture(self):
        """
        Get the user's profile picture
        """
        return GooglePicture(self.base.get("picture", []))

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

from temboo.outputs.Google.Drive.GooglePicture import GooglePicture