# coding: utf-8

class FacebookTag:
    """
     An object containing a tagged user and their position in this photo
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedTime(self):
        """
        The timestamp when this tag was created in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getId(self):
        """
        The id of person who is tagged
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of ther person who is tagged
        """
        return self.base.get("name", [])

    def getX(self):
        """
        The x coordinate which indicates the position in the photo
        """
        return self.base.get("x", [])

    def getY(self):
        """
        The y coordinate which indicates the position in the photo
        """
        return self.base.get("y", [])

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

