# coding: utf-8

class FoursquareRecommendationItem:
    """

          
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getReasons(self):
        """
        Get reasons why this place may be of interest to the acting user
        """
        return [FoursquareReason(le) for le in self.getJSONObject(self.base, "reasons").get("items", [])]


    def getTips(self):
        """
        Get suggested tips
        """
        return [FoursquareTip(le) for le in self.base.get("tips", [])]


    def getVenue(self):
        """
        Get suggested venues
        """
        return FoursquareVenue(self.base.get("venue", []))

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

from temboo.outputs.Foursquare.FoursquareReason import FoursquareReason
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue