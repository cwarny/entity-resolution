# coding: utf-8

class FacebookUser:
    """
     A user object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getBirthday(self):
        """
        The user's date of birth
        """
        return self.base.get("birthday", [])

    def getEducation(self):
        """
        Get the user's education information
        """
        return [FacebookEducation(le) for le in self.base.get("education", [])]


    def getEmail(self):
        """
        The user's email address
        """
        return self.base.get("email", [])

    def getFirstName(self):
        """
        the user's first name
        """
        return self.base.get("first_name", [])

    def getGender(self):
        """
        The user's gender
        """
        return self.base.get("gender", [])

    def getId(self):
        """
        The id of the user
        """
        return self.base.get("id", [])

    def getLastName(self):
        """
        The last name of the user
        """
        return self.base.get("last_name", [])

    def getLink(self):
        """
        The link the the user's profile page
        """
        return self.base.get("link", [])

    def getLocale(self):
        """
        The user's locale
        """
        return self.base.get("locale", [])

    def getUserLocation(self):
        """
        Get the location information
        """
        return FacebookUserLocation(self.base.get("location", []))

    def getName(self):
        """
        The name of the user
        """
        return self.base.get("name", [])

    def getRelationshipStatus(self):
        """
        The relationship status of the user
        """
        return self.base.get("relationship_status", [])

    def getSignificantOther(self):
        """
        Get the id and name of the user's significant other
        """
        return FacebookSignificantOther(self.base.get("significant_other", []))

    def getTimezone(self):
        """
        The user's timezone offset from UTC
        """
        return self.base.get("timezone", [])

    def getUpdatedTime(self):
        """
        The last time the user's profile was updated;
        """
        return self.base.get("updated_time", [])

    def getUsername(self):
        """
        The user's Facebook username
        """
        return self.base.get("username", [])

    def getVerified(self):
        """
        The user's account verification status, either true or false
        """
        return self.base.get("verified", [])

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

from temboo.outputs.Facebook.FacebookEducation import FacebookEducation
from temboo.outputs.Facebook.FacebookSignificantOther import FacebookSignificantOther
from temboo.outputs.Facebook.FacebookUserLocation import FacebookUserLocation