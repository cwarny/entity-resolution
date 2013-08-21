# coding: utf-8

class StripePeriod:
    """
     Covers a billing period for a Subscription or InvoiceItem

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getEnd(self):
        """
        timestamp of the end of billing period.
        """
        return self.base.get("end", [])

    def getStart(self):
        """
        timestamp of the start of the billing period.
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

