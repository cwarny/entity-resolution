# coding: utf-8

class StripeAccountDetails:
    """
     This is an object representing your Stripe account. You can retrieve it to see properties on the account like its current e-mail address or if the account is enabled yet to make live charges.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getChargeEnabled(self):
        """
        Whether or not the account can create live charges
        """
        return self.base.get("charge_enabled", [])

    def getCurrenciesSupported(self):
        """
        The currencies this account can submit when creating charges
        """
        return [le for le in self.base.get("currencies_supported", [])]


    def getDetailsSubmitted(self):
        """
        Whether or not account details have been submitted yet
        """
        return self.base.get("details_submitted", [])

    def getEmail(self):
        """
        The primary user's email address
        """
        return self.base.get("email", [])

    def getId(self):
        """
        A unique identifier for the account
        """
        return self.base.get("id", [])

    def getObject(self):
        """
        Value is "account"
        """
        return self.base.get("object", [])

    def getStatementDescriptor(self):
        """
        The text that will appear on credit card statements
        """
        return self.base.get("statement_descriptor", [])

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

