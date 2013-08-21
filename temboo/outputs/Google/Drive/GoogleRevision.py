# coding: utf-8

class GoogleRevision:
    """
     An object representing a revision of a file

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEtag(self):
        """
        The ETag of the revision
        """
        return self.base.get("etag", [])

    def getExportLinks(self):
        """
        Get links for exporting Google Docs to specific formats
        """
        return GoogleExportLinks(self.base.get("exportLinks", []))

    def getId(self):
        """
        The ID of the revision
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        This is always drive#revision
        """
        return self.base.get("kind", [])

    def getLastModifyingUserName(self):
        """
        Name of the last user to modify this revision
        """
        return self.base.get("lastModifyingUserName", [])

    def getMimeType(self):
        """
        The MIME type of the revision
        """
        return self.base.get("mimeType", [])

    def getModifiedDate(self):
        """
        Last time this revision was modified (formatted RFC 3339 timestamp)
        """
        return self.base.get("modifiedDate", [])

    def getPublished(self):
        """
        Whether this revision is published
        """
        return self.base.get("published", [])

    def getSelfLink(self):
        """
        A link back to this revision
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

from temboo.outputs.Google.Drive.GoogleExportLinks import GoogleExportLinks