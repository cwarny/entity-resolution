# coding: utf-8

class FacebookLike:
    """
     An object containing the id and name of the user who liked a post

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCategory(self):
        """
        The category of the item that was liked. May not be present in the response
        """
        return self.base.get("category", [])

    def getCreatedTime(self):
        """
        The date and time that the object was liked in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getId(self):
        """
        The id of the user who liked an object
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the user who liked an object
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

