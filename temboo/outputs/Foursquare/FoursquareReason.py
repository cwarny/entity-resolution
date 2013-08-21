# coding: utf-8

class FoursquareReason:
    """
     Contains information about why this place may be of interest to the acting user
            
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getMessage(self):
        """
        The message text for the reason
        """
        return self.base.get("message", [])

    def getType(self):
        """
        The reason type
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

