# coding: utf-8

class GoogleCommentList:
    """
     A list of comments for a file

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getComments(self):
        """
        A Google Drive comment resource
        """
        return [GoogleComment(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        This is always drive#commentList
        """
        return self.base.get("kind", [])

    def getNextPageToken(self):
        """
        The page token for the next page of comments
        """
        return self.base.get("nextPageToken", [])

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

from temboo.outputs.Google.Drive.GoogleComment import GoogleComment