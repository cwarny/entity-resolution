# coding: utf-8

class StripeChargeList:
    """
     Returns a list of charges you've previously created. The charges are returned in sorted order, with the most recent charges appearing first.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getCount(self):
        """
        A limit on the number of objects to be returned. Count can range between 1 and 100 items.
        """
        return self.base.get("count", [])

    def getCharges(self):
        """
        The Stripe Charge object
        """
        return [StripeCharge(le) for le in self.base.get("data", [])]


    def getObject(self):
        """
        Value is always "list"
        """
        return self.base.get("object", [])

    def getUrl(self):
        """
        URL to the REST API call
        """
        return self.base.get("url", [])

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

from temboo.outputs.Stripe.StripeCharge import StripeCharge