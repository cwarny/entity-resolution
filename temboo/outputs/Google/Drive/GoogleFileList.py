# coding: utf-8

class GoogleFileList:
    """
     A listing of files in Google Drive

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

    def getFiles(self):
        """
        A Google Drive file resource
        """
        return [GoogleFile(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        The type of resource (this is always rive#fileList)
        """
        return self.base.get("kind", [])

    def getNextLink(self):
        """
        A link to the next page of files
        """
        return self.base.get("nextLink", [])

    def getNextPageToken(self):
        """
        The page token for the next page of files
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

from temboo.outputs.Google.Drive.GoogleFile import GoogleFile