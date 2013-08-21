# coding: utf-8

class FoursquareForeignIds:
    """
     Contains the domain and id of the third party provider
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDomain(self):
        """
        The domain of the 3rd party provider
        """
        return self.base.get("domain", [])

    def getId(self):
        """
        The id of the 3rd party provider
        """
        return self.base.get("id", [])

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

