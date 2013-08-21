# coding: utf-8

class FoursquareHours:
    """
     Contains the hours during the week that the venue is open along with any named hours segments in a human-readable format
      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getIsOpen(self):
        """
        Whether or not the venue is open
        """
        return self.base.get("isOpen", [])

    def getStatus(self):
        """
        The venue status
        """
        return self.base.get("status", [])

    def getTimeframes(self):
        """
        Get the timeframe information for the venue including days of operation
        """
        return [FoursquareTimeframe(le) for le in self.base.get("timeframes", [])]


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

from temboo.outputs.Foursquare.FoursquareTimeframe import FoursquareTimeframe