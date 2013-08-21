# coding: utf-8

class FoursquareUser:
    """
     A user object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBio(self):
        """
        The bio of the user
        """
        return self.base.get("bio", [])

    def getContact(self):
        """
        An object containing twitter, phone, and formattedPhone of the user
        """
        return FoursquareContact(self.base.get("contact", []))

    def getFirstName(self):
        """
        """
        return self.base.get("firstName", [])

    def getGender(self):
        """
        """
        return self.base.get("gender", [])

    def getHomeCity(self):
        """
        """
        return self.base.get("homeCity", [])

    def getId(self):
        """
        """
        return self.base.get("id", [])

    def getLastName(self):
        """
        """
        return self.base.get("lastName", [])

    def getListGroup(self):
        return [FoursquareListGroup(le) for le in self.getJSONObject(self.base, "lists").get("groups", [])]


    def getPhoto(self):
        """
        """
        return self.base.get("photo", [])

    def getTipsCount(self):
        """
        Contains the total count of tips and groups with friends and others
        """
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

from temboo.outputs.Foursquare.FoursquareContact import FoursquareContact
from temboo.outputs.Foursquare.FoursquareListGroup import FoursquareListGroup
from temboo.outputs.Foursquare.FoursquareTipsCount import FoursquareTipsCount