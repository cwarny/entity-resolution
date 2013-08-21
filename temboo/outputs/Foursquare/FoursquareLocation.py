# coding: utf-8

class FoursquareLocation:
    """
     Contains location information for the venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAddress(self):
        """
        The venue address
        """
        return self.base.get("address", [])

    def getCc(self):
        """
        The country abbreviation field for the venue address
        """
        return self.base.get("cc", [])

    def getCity(self):
        """
        The city that the venue is in
        """
        return self.base.get("city", [])

    def getCountry(self):
        """
        The country field for the venue address
        """
        return self.base.get("country", [])

    def getCrossStreet(self):
        """
        The cross street of the venue
        """
        return self.base.get("crossStreet", [])

    def getLat(self):
        """
        The latitude coordinate for the venue
        """
        return self.base.get("lat", [])

    def getLng(self):
        """
        The longitude coordinate for the venue
        """
        return self.base.get("lng", [])

    def getPostalCode(self):
        """
        The postal code of the venue
        """
        return self.base.get("postalCode", [])

    def getState(self):
        """
        The state that the venue is in
        """
        return self.base.get("state", [])

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

