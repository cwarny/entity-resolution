# coding: utf-8

class FacebookLocation:
    """
     An object containing location information for the place
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCity(self):
        """
        The city that the place is located in
        """
        return self.base.get("city", [])

    def getCountry(self):
        """
        The country that the place is located in
        """
        return self.base.get("country", [])

    def getLatitude(self):
        """
        The latitude coordinate
        """
        return self.base.get("latitude", [])

    def getLongitude(self):
        """
        The longitude coordinate
        """
        return self.base.get("longitude", [])

    def getState(self):
        """
        The state abbreviation for the place
        """
        return self.base.get("state", [])

    def getStreet(self):
        """
        The street address for the place
        """
        return self.base.get("street", [])

    def getZip(self):
        """
        The zip code for the place
        """
        return self.base.get("zip", [])

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

