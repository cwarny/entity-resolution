# coding: utf-8

class FoursquareListFollower:
    """
     Contains the followers of the list
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCanonicalUrl(self):
        """
        The canonical URL for the user following the list
        """
        return self.base.get("canonicalUrl", [])

    def getFirstName(self):
        """
        The first name of the user following the list
        """
        return self.base.get("firstName", [])

    def getGender(self):
        """
        The gender of the user who is following the list
        """
        return self.base.get("gender", [])

    def getHomeCity(self):
        """
        The home city of the user who is following the list
        """
        return self.base.get("homeCity", [])

    def getId(self):
        """
        The id of the user who is following the list
        """
        return self.base.get("id", [])

    def getLastName(self):
        """
        The last name of the user who is following the list
        """
        return self.base.get("lastName", [])

    def getPhoto(self):
        """
        The url to the photo of the follower
        """
        return self.base.get("photo", [])

    def getTipsCount(self):
        return FoursquareTipsCount(self.base.get("tips", []))

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

from temboo.outputs.Foursquare.FoursquareTipsCount import FoursquareTipsCount