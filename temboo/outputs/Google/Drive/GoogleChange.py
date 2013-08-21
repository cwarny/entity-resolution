# coding: utf-8

class GoogleChange:
    """
     An object representing a change for a Google Drive resource

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDeleted(self):
        """
        Whether the file has been deleted
        """
        return self.base.get("deleted", [])

    def getFileId(self):
        """
        The ID of the file associated with this change
        """
        return self.base.get("fileId", [])

    def getId(self):
        """
        The ID of the change
        """
        return self.base.get("id", [])

    def getKind(self):
        """
        This is always drive#change
        """
        return self.base.get("kind", [])

    def getSelfLink(self):
        """
        A link back to this change
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

