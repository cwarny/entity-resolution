# coding: utf-8

class FoursquareOpen:
    """
     The segments of the days in this timeframe in which the venue is open
          
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEnd(self):
        """
        The time the venue closes in HHMM (24hr) format
        """
        return self.base.get("end", [])

    def getRenderedTime(self):
        """
        The human readable version the open and close times
        """
        return self.base.get("renderedTime", [])

    def getStart(self):
        """
        The time the venue opens in HHMM (24hr) format
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

