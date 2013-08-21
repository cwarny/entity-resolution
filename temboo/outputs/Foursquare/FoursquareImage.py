# coding: utf-8

class FoursquareImage:
    """

            
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getName(self):
        """
        The name of the image used to contruct the complete image url
        """
        return self.base.get("name", [])

    def getPrefix(self):
        """
        The beginning portion of the image url used to contruct the complete image url
        """
        return self.base.get("prefix", [])

    def getSizes(self):
        """
        The available image sizes used to construct the complete image url
        """
        return [le for le in self.base.get("sizes", [])]


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

