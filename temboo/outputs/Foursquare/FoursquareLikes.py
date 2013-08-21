# coding: utf-8

class FoursquareLikes:
    """
     Contains a count and group of people who liked an object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        The count of users liked the object
        """
        return self.base.get("count", [])

    def getPeopleGroups(self):
        """
        Contains groups of friends and others that have liked an object
        """
        return [FoursquarePeopleGroup(le) for le in self.base.get("groups", [])]


    def getSummary(self):
        """
        The summary of likes
        """
        return self.base.get("summary", [])

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

from temboo.outputs.Foursquare.FoursquarePeopleGroup import FoursquarePeopleGroup