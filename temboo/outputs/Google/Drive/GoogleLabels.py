# coding: utf-8

class GoogleLabels:
    """
     A label for the file
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getHidden(self):
        """
        Whether or not the file is hidden
        """
        return self.base.get("hidden", [])

    def getRestricted(self):
        """
        Whether or not the file is restricted
        """
        return self.base.get("restricted", [])

    def getStarred(self):
        """
        Whether or not the file is starred
        """
        return self.base.get("starred", [])

    def getTrashed(self):
        """
        Whether or not the file is trashed
        """
        return self.base.get("trashed", [])

    def getViewed(self):
        """
        Whether or not the file is viewed
        """
        return self.base.get("viewed", [])

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

