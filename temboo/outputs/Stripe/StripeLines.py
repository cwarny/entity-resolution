# coding: utf-8

class StripeLines:
    """

      
    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getInvoiceItems(self):
        """
        """
        return [StripeInvoiceItem(le) for le in self.base.get("invoiceitems", [])]


    def getSubscriptions(self):
        """
        """
        return [StripeSubscription(le) for le in self.base.get("subscriptions", [])]


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

from temboo.outputs.Stripe.StripeInvoiceItem import StripeInvoiceItem
from temboo.outputs.Stripe.StripeSubscription import StripeSubscription