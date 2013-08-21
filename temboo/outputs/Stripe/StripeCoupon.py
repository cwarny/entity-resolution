# coding: utf-8

class StripeCoupon:
    """
     class Coupon coupon /_ // A coupon contains information about a percent-off discount you might want to apply to a customer. Coupons only apply to invoices created for recurring subscriptions and invoice items; they do not apply to one-off charges.


    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAmountOff(self):
        """
        Amount (in the currency specified)
        """
        return self.base.get("amount_off", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code) If amount_off has been set, the currency of the amount to take off.
        """
        return self.base.get("currency", [])

    def getDuration(self):
        """
        One of forever, once, and repeating. Describes how long a customer who applies this coupon will get the discount.
        """
        return self.base.get("duration", [])

    def getDurationInMonths(self):
        """
        If duration is repeating, the number of months the coupon applies. Null if coupon duration is forever or once.
        """
        return self.base.get("duration_in_months", [])

    def getId(self):
        """
        the ID of coupon
        """
        return self.base.get("id", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getMaxRedemptions(self):
        """
        Maximum number of times this coupon can be redeemed by a customer before it is no longer valid.
        """
        return self.base.get("max_redemptions", [])

    def getObject(self):
        """
        Value is always "coupon"
        """
        return self.base.get("object", [])

    def getPercentOff(self):
        """
        Percent that will be taken off the subtotal of any invoices for this customer for the duration of the coupon. For example, a coupon with percent_off of 50 will make a $100 invoice $50 instead.
        """
        return self.base.get("percent_off", [])

    def getRedeemBy(self):
        """
        Date after which the coupon can no longer be redeemed
        """
        return self.base.get("redeem_by", [])

    def getTimesRedeemed(self):
        """
        Number of times this coupon has been applied to a customer.
        """
        return self.base.get("times_redeemed", [])

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

