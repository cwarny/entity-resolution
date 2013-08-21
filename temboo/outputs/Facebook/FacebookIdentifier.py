# coding: utf-8

class FacebookIdentifier:
    """
     A generic itentifier for a Facebook object, consisting of a name and ID.
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getId(self):
        """
        Object ID
        """
        return self.base.get("id", [])

    def getName(self):
        """
        Object name
        """
        return self.base.get("name", [])

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

