# coding: utf-8

class GoogleCreator:
    """
     The creator of the event
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEmail(self):
        """
        The creator's email address, if available.
        """
        return self.base.get("email", [])

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

