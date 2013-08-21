# coding: utf-8

class StripePlan:
    """
     class Plan plan /_ // A subscription plan contains the pricing information for different products and feature levels on your site. For example, you might have a $10/month plan for basic features and a different $20/month plan for premium features.


    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAmount(self):
        """
        The amount in cents to be charged on the interval specified
        """
        return self.base.get("amount", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code) Currency in which subscription will be charged
        """
        return self.base.get("currency", [])

    def getId(self):
        """
        the ID of the Plan
        """
        return self.base.get("id", [])

    def getInterval(self):
        """
        One of month or year. The frequency with which a subscription should be billed.
        """
        return self.base.get("interval", [])

    def getIntervalCount(self):
        """
        The number of the unit specified in the interval parameter. For example, you could specify an interval_count of 3 and an interval of 'month' for quarterly billing (every 3 months).
        """
        return self.base.get("interval_count", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getName(self):
        """
        Display name of the plan
        """
        return self.base.get("name", [])

    def getObject(self):
        """
        Value is always "plan"
        """
        return self.base.get("object", [])

    def getTrialPeriodDays(self):
        """
        Number of trial period days granted when subscribing a customer to this plan. Null if the plan has no trial period
        """
        return self.base.get("trial_period_days", [])

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

