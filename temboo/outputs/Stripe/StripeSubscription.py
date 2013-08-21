# coding: utf-8

class StripeSubscription:
    """
     Subscriptions allow you to charge a customer's card on a recurring basis. A subscription ties a customer to a particular plan you've created.

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

    def getCancelAtPeriodEnd(self):
        """
        If the subscription has been canceled with the at_period_end flag set to true, cancel_at_period_end on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period.
        """
        return self.base.get("cancel_at_period_end", [])

    def getCanceledAt(self):
        """
        If the subscription has been canceled, the date of that cancellation. If the subscription was canceled with cancel_at_period_end, canceled_at will still reflect the date of the initial cancellation request, not the end of the subscription period when the subscription is automatically moved to a canceled state.
        """
        return self.base.get("canceled_at", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getCurrentPeriodEnd(self):
        """
        End of the current period that the subscription has been invoiced for. At the end of this period, a new invoice will be created.
        """
        return self.base.get("current_period_end", [])

    def getCurrentPeriodStart(self):
        """
        Start of the current period that the subscription has been invoiced for
        """
        return self.base.get("current_period_start", [])

    def getCustomer(self):
        """
        Object describing the customer
        """
        return self.base.get("customer", [])

    def getDescription(self):
        """
        description of the Subscription
        """
        return self.base.get("description", [])

    def getEndedAt(self):
        """
        If the subscription has ended (either because it was canceled or because the customer was switched to a subscription to a new plan), the date the subscription ended
        """
        return self.base.get("ended_at", [])

    def getId(self):
        """
        ID of the subscription
        """
        return self.base.get("id", [])

    def getObject(self):
        """
        Value always "subscription"
        """
        return self.base.get("object", [])

    def getPeriod(self):
        """
        The period this subscription covers
        """
        return StripePeriod(self.base.get("period", []))

    def getPlan(self):
        """
        Object describing the plan the customer is subscribed to
        """
        return StripePlan(self.base.get("plan", []))

    def getProration(self):
        """
        Whether or not this is a proration
        """
        return self.base.get("proration", [])

    def getQuantity(self):
        """
        number of subscriptions
        """
        return self.base.get("quantity", [])

    def getStart(self):
        """
        timestamp.  Date the subscription started
        """
        return self.base.get("start", [])

    def getStatus(self):
        """
        Possible values are trialing, active, past_due, canceled, or unpaid. A subscription still in its trial period is trialing and moves to active when the trial period is over. When payment to renew the subscription fails, the subscription becomes past_due. After Stripe has exhausted all payment retry attempts, the subscription ends up with a status of either canceled or unpaid depending on your retry settings. Note that when a subscription has a status of unpaid, any future invoices will not be attempted until the customer's card details are updated.
        """
        return self.base.get("status", [])

    def getTrialEnd(self):
        """
        If the subscription has a trial, the end of that trial.
        """
        return self.base.get("trial_end", [])

    def getTrialStart(self):
        """
        If the subscription has a trial, the beginning of that trial.
        """
        return self.base.get("trial_start", [])

    def getType(self):
        """
        the Type of the object
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

from temboo.outputs.Stripe.StripePeriod import StripePeriod
from temboo.outputs.Stripe.StripePlan import StripePlan