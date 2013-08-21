# coding: utf-8

class FacebookEducation:
    """
     An entry from a user's education history
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getSchool(self):
        """
        Get the school for this user
        """
        return FacebookSchool(self.base.get("school", []))

    def getType(self):
        """
        The type of school
        """
        return self.base.get("type", [])

    def getYear(self):
        """
        Get the graduation year info for a user's school
        """
        return FacebookYear(self.base.get("year", []))

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

from temboo.outputs.Facebook.FacebookSchool import FacebookSchool
from temboo.outputs.Facebook.FacebookYear import FacebookYear