# coding: utf-8

class GoogleParentList:
    """
     A list of parent resources

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

    def getParents(self):
        """
        A Google Drive parent resource
        """
        return [GoogleParent(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        The type of resource (this is always drive#parentList)
        """
        return self.base.get("kind", [])

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

from temboo.outputs.Google.Drive.GoogleParent import GoogleParent