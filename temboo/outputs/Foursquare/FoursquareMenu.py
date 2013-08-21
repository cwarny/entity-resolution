# coding: utf-8

class FoursquareMenu:
    """
     An object containing url and mobileUrl that display the menu information for this venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getMobileUrl(self):
        """
        The mobile url of the menu
        """
        return self.base.get("mobileUrl", [])

    def getType(self):
        """
        The type of menu
        """
        return self.base.get("type", [])

    def getUrl(self):
        """
        The url for the menu
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

