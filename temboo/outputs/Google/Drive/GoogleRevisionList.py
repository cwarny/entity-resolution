# coding: utf-8

class GoogleRevisionList:
    """
     A list of a file's revisions

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

    def getRevisions(self):
        """
        Get a revision for a file
        """
        return [GoogleRevision(le) for le in self.base.get("items", [])]


    def getKind(self):
        """
        This is always drive#revisionList
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

from temboo.outputs.Google.Drive.GoogleRevision import GoogleRevision