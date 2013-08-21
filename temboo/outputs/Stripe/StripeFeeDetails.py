# coding: utf-8

class StripeFeeDetails:
    """
     Detailed breakdown of fees (in cents) paid for this charge  
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAmount(self):
        """
        Amount (in the currency specified)
        """
        return self.base.get("amount", [])

    def getAmountRefunded(self):
        """
        Amount in cents refunded (can be less than the amount attribute on the charge if a partial refund was issued)
        """
        return self.base.get("amount_refunded", [])

    def getApplication(self):
        """
        """
        return self.base.get("application", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getDescription(self):
        """
        description of the fee
        """
        return self.base.get("description", [])

    def getType(self):
        """
        value always "stripe_fee"
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

