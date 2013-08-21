# coding: utf-8

class FoursquareListGroup:
    """
     Contains groups of list including created, edited, followed, friends, or other

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        The count of groups returned
        """
        return self.base.get("count", [])

    def getLists(self):
        """
        Get lists
        """
        return [FoursquareList(le) for le in self.base.get("items", [])]


    def getType(self):
        """
        The type of group
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

from temboo.outputs.Foursquare.FoursquareList import FoursquareList