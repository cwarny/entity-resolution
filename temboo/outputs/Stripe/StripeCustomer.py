# coding: utf-8

class StripeCustomer:
    """


    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAccountBalance(self):
        """
        Current balance, if any, being stored on the customer's account. If negative, the customer has credit to apply to the next invoice. If positive, the customer has an amount owed that will be added to the next invoice. The balance does not refer to any unpaid invoices; it solely takes into account amounts that have yet to be successfully applied to any invoice. This balance is only taken into account for recurring charges.
        """
        return self.base.get("account_balance", [])

    def getActiveCard(self):
        """
        Object describing the current card on the customer, if there is one.
        """
        return StripeCard(self.base.get("active_card", []))

    def getCreated(self):
        """
        timestamp of when Customer was created
        """
        return self.base.get("created", [])

    def getDescription(self):
        """
        description of the Customer
        """
        return self.base.get("description", [])

    def getEmail(self):
        """
        e-mail address of the Customer
        """
        return self.base.get("email", [])

    def getId(self):
        """
        ID of the Customer
        """
        return self.base.get("id", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getNextRecurringCharge(self):
        """
        """
        return StripeNextRecurringCharge(self.base.get("next_recurring_charge", []))

    def getObject(self):
        """
        Value is always "customer"
        """
        return self.base.get("object", [])

    def getSubscription(self):
        """
        Object describing the Subscription type
        """
        return StripeSubscription(self.base.get("subscription", []))

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
from temboo.outputs.Stripe.StripeNextRecurringCharge import StripeNextRecurringCharge
from temboo.outputs.Stripe.StripeSubscription import StripeSubscription