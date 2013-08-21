# coding: utf-8

class StripeToken:
    """
      Often you want to be able to charge credit cards without having to hold sensitive card information on your own servers. Stripe.js makes this easy in the browser, but you can use the same technique in other environments with our card token API. Card tokens can be created with your publishable API key, which can safely be embedded in downloadable applications like iPhone and Android apps. You can then use a token anywhere in our API that a card is accepted. Note that tokens are not meant to be stored or used more than once -- to store payment details for use later, you should create a Customer object.

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

    def getCard(self):
        """
        Object describing the card used to make the charge
        """
        return StripeCard(self.base.get("card", []))

    def getCreated(self):
        """
        Object describing the card used to make the charge
        """
        return self.base.get("created", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getId(self):
        """
        ID of the Token
        """
        return self.base.get("id", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getObject(self):
        """
        Value is always "token"
        """
        return self.base.get("object", [])

    def getUsed(self):
        """
        Whether or not this token has already been used (tokens can be used only once)
        """
        return self.base.get("used", [])

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