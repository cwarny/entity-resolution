# coding: utf-8

class StripeInvoiceItem:
    """
     An Invoice Line Item

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

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getCustomer(self):
        """
        ID of the Customer
        """
        return self.base.get("customer", [])

    def getDate(self):
        """
        timestamp
        """
        return self.base.get("date", [])

    def getDescription(self):
        """
        A text description of the line item
        """
        return self.base.get("description", [])

    def getId(self):
        """
        The ID of the source of this line item, either an invoice item or a subscription
        """
        return self.base.get("id", [])

    def getInvoice(self):
        """
        ID of the invoice
        """
        return self.base.get("invoice", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getObject(self):
        """
        value is always "invoiceitem"
        """
        return self.base.get("object", [])

    def getPeriod(self):
        """
        The period this InvoiceItme covers
        """
        return StripePeriod(self.base.get("period", []))

    def getPlan(self):
        """
        The plan of the subscription, if the line item is a subscription
        """
        return StripePlan(self.base.get("plan", []))

    def getProration(self):
        """
        Whether or not this is a proration
        """
        return self.base.get("proration", [])

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

from temboo.outputs.Stripe.StripePeriod import StripePeriod
from temboo.outputs.Stripe.StripePlan import StripePlan