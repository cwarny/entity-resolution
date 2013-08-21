# coding: utf-8

class FoursquareContact:
    """
     An object containing twitter, phone, and formattedPhone of the user or venue contact. All can be present, and all can be absent from the response.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEmail(self):
        """
        The email address of the contact
        """
        return self.base.get("email", [])

    def getFacebook(self):
        """
        The facebook id of the contact
        """
        return self.base.get("facebook", [])

    def getFormattedPhone(self):
        """
        The formatted phone number of the contact
        """
        return self.base.get("formattedPhone", [])

    def getPhone(self):
        """
        The unformatted phone number of the contact
        """
        return self.base.get("phone", [])

    def getTwitter(self):
        """
        The twitter handle of the contact
        """
        return self.base.get("twitter", [])

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

