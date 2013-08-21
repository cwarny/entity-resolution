# coding: utf-8

class FoursquareSegment:
    """
     Contains the named segments of the days in this timeframe in which the venue is open
          
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEnd(self):
        """
        The time as HHMM (24hr) at which the segment ends
        """
        return self.base.get("end", [])

    def getStart(self):
        """
        The time as HHMM (24hr) at which the segment begins
        """
        return self.base.get("start", [])

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

