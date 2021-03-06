# coding: utf-8

class FoursquareSize:
    """
     Available sizes for an image

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getHeight(self):
        """
        The height of an image
        """
        return self.base.get("height", [])

    def getUrl(self):
        """
        The url for an image
        """
        return self.base.get("url", [])

    def getWidth(self):
        """
        The width of the image
        """
        return self.base.get("width", [])

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

