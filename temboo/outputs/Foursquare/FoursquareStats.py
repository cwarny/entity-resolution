# coding: utf-8

class FoursquareStats:
    """
     Contains statistics for the venue including checkinsCount, tipCount, and userCount

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCheckinsCount(self):
        """
        The total number of checkins for this venue
        """
        return self.base.get("checkinsCount", [])

    def getTipCount(self):
        """
        The number of tips for this venue
        """
        return self.base.get("tipCount", [])

    def getUsersCount(self):
        """
        The total number of users that have checked into this venue
        """
        return self.base.get("usersCount", [])

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

