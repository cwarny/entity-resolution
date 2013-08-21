# coding: utf-8

class FoursquareTimeframe:
    """
     An object containing the days
        
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getDays(self):
        """
        Days represented as integers with Monday = 1,..., Sunday = 7 on which these hours apply
        """
        return self.base.get("days", [])

    def getIncludesToday(self):
        """
        Indicates if this timeframe includes today
        """
        return self.base.get("includesToday", [])

    def getOpen(self):
        """
        Get the start, end, and rendered time for the venue
        """
        return [FoursquareOpen(le) for le in self.base.get("open", [])]


    def getSegments(self):
        """
        Get segment information for the venue
        """
        return [FoursquareSegment(le) for le in self.base.get("segments", [])]


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

from temboo.outputs.Foursquare.FoursquareOpen import FoursquareOpen
from temboo.outputs.Foursquare.FoursquareSegment import FoursquareSegment