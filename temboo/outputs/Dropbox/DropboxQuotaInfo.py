# coding: utf-8

class DropboxQuotaInfo:
    """
     The user's quota info for shared/unshared folders
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getNormal(self):
        """
        The user's used quota outside of shared folders (bytes).
        """
        return self.base.get("normal", [])

    def getQuota(self):
        """
        The user's used quota in shared folders (bytes).
        """
        return self.base.get("quota", [])

    def getShared(self):
        """
        The user's total quota allocation (bytes).
        """
        return self.base.get("shared", [])

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

