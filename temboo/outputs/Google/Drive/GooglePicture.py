# coding: utf-8

class GooglePicture:
    """
     An object representing the user's profile picture
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getUrl(self):
        """
        A URL that points to a profile picture of this user
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

