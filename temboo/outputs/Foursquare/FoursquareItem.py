# coding: utf-8

class FoursquareItem:
    """
     A list item object

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDone(self):
        """
        Whether or not this item has been done
        """
        return self.base.get("done", [])

    def getId(self):
        """
        The id of the item
        """
        return self.base.get("id", [])

    def getListed(self):
        """
        Get lists for the authenticated user
        """
        return FoursquareListed(self.base.get("listed", []))

    def getTip(self):
        """
        Get the tip for this item
        """
        return FoursquareTip(self.base.get("tip", []))

    def getTodo(self):
        """
        Whether or not this item is a todo
        """
        return self.base.get("todo", [])

    def getVenue(self):
        """
        Get the venue that this item is for
        """
        return FoursquareVenue(self.base.get("venue", []))

    def getVisitedCount(self):
        """
        How many times the venue is has been visited
        """
        return self.base.get("visitedCount", [])

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

from temboo.outputs.Foursquare.FoursquareListed import FoursquareListed
from temboo.outputs.Foursquare.FoursquareTip import FoursquareTip
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue