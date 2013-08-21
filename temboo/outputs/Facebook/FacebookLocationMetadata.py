# coding: utf-8

class FacebookLocationMetadata:
    """
     An object associated with a location

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getApplication(self):
        """
        Get the application that created this object
        """
        return FacebookApplication(self.base.get("application", []))

    def getCreatedTime(self):
        """
        The creation time of this object
        """
        return self.base.get("created_time", [])

    def getFrom(self):
        """
        Get the user that the object is from
        """
        return FacebookFrom(self.getJSONObject(self.base, "from").get("from", []))

    def getId(self):
        """
        The id of this object
        """
        return self.base.get("id", [])

    def getPlace(self):
        """
        Get the place and location for this graph object
        """
        return FacebookPlace(self.base.get("place", []))

    def getType(self):
        """
        The type of object
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

from temboo.outputs.Facebook.FacebookApplication import FacebookApplication
from temboo.outputs.Facebook.FacebookFrom import FacebookFrom
from temboo.outputs.Facebook.FacebookPlace import FacebookPlace