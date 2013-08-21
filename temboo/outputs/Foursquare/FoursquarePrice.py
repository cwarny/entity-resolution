# coding: utf-8

class FoursquarePrice:
    """
     Contains price information for this venue
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getMessage(self):
        """
        The message for pricing
        """
        return self.base.get("message", [])

    def getTier(self):
        """
        The pricing tier
        """
        return self.base.get("tier", [])

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

