# coding: utf-8

class FoursquareListed:
    """
     Contains a count of lists that contain this venue

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        A count of lists
        """
        return self.base.get("count", [])

    def getListedItems(self):
        return [FoursquareListedItems(le) for le in self.base.get("items", [])]


    def getSummary(self):
        """
        A summary field for the listed items
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

from temboo.outputs.Foursquare.FoursquareListedItems import FoursquareListedItems