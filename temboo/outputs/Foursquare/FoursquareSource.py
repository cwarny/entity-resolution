# coding: utf-8

class FoursquareSource:
    """
     An object containing the source information about this object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDetailUrl(self):
        """
        The detail url for the application that created the object
        """
        return self.base.get("detailUrl", [])

    def getIcon(self):
        """
        The icon for the application that create the object
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        The id of the application that created the object
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the application that created the object
        """
        return self.base.get("name", [])

    def getPhoto(self):
        """
        The link to the photo of the application that created the object
        """
        return self.base.get("photo", [])

    def getUrl(self):
        """
        The url for the application that created the object
        """
        return self.base.get("url", [])

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

