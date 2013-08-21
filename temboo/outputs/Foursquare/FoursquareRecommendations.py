# coding: utf-8

class FoursquareRecommendations:
    """
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getRecommendationGroups(self):
        return [FoursquareRecommendationGroup(le) for le in self.base.get("groups", [])]


    def getHeaderFullLocation(self):
        """
        A full text name for the location the user searched
        """
        return self.base.get("headerFullLocation", [])

    def getHeaderLocation(self):
        """
        A text name for the location the user searched
        """
        return self.base.get("headerLocation", [])

    def getHeaderLocationGranularity(self):
        """
        More granular location information
        """
        return self.base.get("headerLocationGranularity", [])

    def getHeaderMessage(self):
        """
        A message to the user based on their current context
        """
        return self.base.get("headerMessage", [])

    def getKeywords(self):
        """
        Get keyword suggestions
        """
        return FoursquareKeywords(self.getJSONObject(self.base, "keywords").get("items", []))

    def getSuggestedRadius(self):
        """
        When no radius is specified, this represents the radius that was used for the query (based upon the density of venues in the query area)
        """
        return self.base.get("suggestedRadius", [])

    def getWarning(self):
        """
        Get warnings about the request
        """
        return FoursquareWarning(self.base.get("warning", []))

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

from temboo.outputs.Foursquare.FoursquareKeywords import FoursquareKeywords
from temboo.outputs.Foursquare.FoursquareRecommendationGroup import FoursquareRecommendationGroup
from temboo.outputs.Foursquare.FoursquareWarning import FoursquareWarning