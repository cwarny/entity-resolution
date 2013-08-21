# coding: utf-8

class FacebookAction:
    """
     An object containing the name and link of an action
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getLink(self):
        """
        The link to the post
        """
        return self.base.get("link", [])

    def getName(self):
        """
        The name of the action
        """
        return self.base.get("name", [])

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

