# coding: utf-8

class FoursquareMeta:
    """
     An object containing the status code from Foursquare

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCode(self):
        """
        The response status code from Foursquare
        """
        return self.base.get("code", [])

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

