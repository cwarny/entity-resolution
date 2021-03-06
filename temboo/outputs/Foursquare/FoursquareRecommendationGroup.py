# coding: utf-8

class FoursquareRecommendationGroup:
    """

        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getRecommendationItem(self):
        return [FoursquareRecommendationItem(le) for le in self.base.get("items", [])]


    def getName(self):
        """
        The name of the group
        """
        return self.base.get("name", [])

    def getType(self):
        """
        The group type
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

from temboo.outputs.Foursquare.FoursquareRecommendationItem import FoursquareRecommendationItem