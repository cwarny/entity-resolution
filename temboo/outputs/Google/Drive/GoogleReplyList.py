# coding: utf-8

class GoogleReplyList:
    """
     A list of replies to a specified comment on a file

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getReplies(self):
        """
        Get a reply to a Google Drive comment
        """
        return [GoogleReply(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        This is always drive#commentReplyList
        """
        return self.base.get("kind", [])

    def getNextLink(self):
        """
        A link to the next page of replies
        """
        return self.base.get("nextLink", [])

    def getNextPageToken(self):
        """
        The page token for the next page of replies
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

from temboo.outputs.Google.Drive.GoogleReply import GoogleReply