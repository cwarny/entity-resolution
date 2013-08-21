# coding: utf-8

class FoursquareSpecial:
    """
     Contains specials offered by a venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDescription(self):
        """
        """
        return self.base.get("description", [])

    def getFinePrint(self):
        """
        """
        return self.base.get("finePrint", [])

    def getIcon(self):
        """
        """
        return self.base.get("icon", [])

    def getId(self):
        """
        """
        return self.base.get("id", [])

    def getMessage(self):
        """
        """
        return self.base.get("message", [])

    def getProvider(self):
        """
        """
        return self.base.get("provider", [])

    def getRedemption(self):
        """
        """
        return self.base.get("redemption", [])

    def getTitle(self):
        """
        """
        return self.base.get("title", [])

    def getType(self):
        """
        """
        return self.base.get("type", [])

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

