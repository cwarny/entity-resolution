# coding: utf-8

class GoogleChildList:
    """
      A listing of child resources

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEtag(self):
        """
        The ETag of the list
        """
        return self.base.get("etag", [])

    def getChildren(self):
        """
        A Google Drive child resource
        """
        return [GoogleChild(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        This is always drive#childList
        """
        return self.base.get("kind", [])

    def getNextLink(self):
        """
        A link to the next page of children
        """
        return self.base.get("nextLink", [])

    def getNextPageToken(self):
        """
        The page token for the next page of children
        """
        return self.base.get("nextPageToken", [])

    def getSelfLink(self):
        """
        A link back to this list
        """
        return self.base.get("selfLink", [])

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

from temboo.outputs.Google.Drive.GoogleChild import GoogleChild