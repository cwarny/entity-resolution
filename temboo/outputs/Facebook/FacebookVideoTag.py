# coding: utf-8

class FacebookVideoTag:
    """
     An object containing a person tagged in a video
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCreatedTime(self):
        """
        The time that the tag was created in in ISO-8601 format
        """
        return self.base.get("created_time", [])

    def getId(self):
        """
        The id of the tag
        """
        return self.base.get("id", [])

    def getName(self):
        """
        The name of the person tagged
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

