# coding: utf-8

class StripeCharge:
    """
     To charge a credit or a debit card, you create a new charge object. You can retrieve and refund individual charges as well as list all charges. Charges are identified by a unique random ID.

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

    def getCaptured(self):
        """
        If the charge was created without capturing, this boolean represents whether or not it is still uncaptured or has since been captured.
        """
        return self.base.get("captured", [])

    def getCard(self):
        """
        Object describing the card used to make the charge
        """
        return StripeCard(self.base.get("card", []))

    def getCreated(self):
        """
        timestamp
        """
        return self.base.get("created", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getCustomer(self):
        """
        ID of the customer this charge is for if one exists
        """
        return self.base.get("customer", [])

    def getDescription(self):
        """
        description of the Charge
        """
        return self.base.get("description", [])

    def getDispute(self):
        """
        Details about the dispute if the charge has been disputed
        """
        return StripeDispute(self.base.get("dispute", []))

    def getDisputed(self):
        """
        Disputed amount. Usually the amount of the charge, but can differ (usually because of currency fluctuation or because only part of the order is disputed).
        """
        return self.base.get("disputed", [])

    def getFailureMessage(self):
        """
        Message to user further explaining reason for charge failure if available
        """
        return self.base.get("failure_message", [])

    def getFee(self):
        """
        The fee (in cents) paid for this charge
        """
        return self.base.get("fee", [])

    def getFeeDetails(self):
        """
        The fee details for this charge
        """
        return [StripeFeeDetails(le) for le in self.base.get("fee_details", [])]


    def getId(self):
        """
        The unique ID of the charge
        """
        return self.base.get("id", [])

    def getInvoice(self):
        """
        ID of the invoice this charge is for if one exists
        """
        return self.base.get("invoice", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getObject(self):
        """
        value is always "charge"
        """
        return self.base.get("object", [])

    def getPaid(self):
        """
        Whether or not payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance.
        """
        return self.base.get("paid", [])

    def getRefunded(self):
        """
        Whether or not the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.
        """
        return self.base.get("refunded", [])

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

from temboo.outputs.Stripe.StripeCard import StripeCard
from temboo.outputs.Stripe.StripeDispute import StripeDispute
from temboo.outputs.Stripe.StripeFeeDetails import StripeFeeDetails