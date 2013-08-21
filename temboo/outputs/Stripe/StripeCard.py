# coding: utf-8

class StripeCard:
    """
     Object describing the card used to make the charge

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAddressCity(self):
        """
        billing address city, if provided when creating card
        """
        return self.base.get("address_city", [])

    def getAddressCountry(self):
        """
        Billing address country, if provided when creating card
        """
        return self.base.get("address_country", [])

    def getAddressLine1(self):
        """
        line 1 of the address
        """
        return self.base.get("address_line1", [])

    def getAddressLine1Check(self):
        """
        If address_line1 was provided, results of the check: pass, fail, or unchecked.
        """
        return self.base.get("address_line1_check", [])

    def getAddressLine2(self):
        """
        line 2 of the address
        """
        return self.base.get("address_line2", [])

    def getAddressState(self):
        """
        """
        return self.base.get("address_state", [])

    def getAddressZip(self):
        """
        zip code
        """
        return self.base.get("address_zip", [])

    def getAddressZipCheck(self):
        """
        If address_zip was provided, results of the check: pass, fail, or unchecked.
        """
        return self.base.get("address_zip_check", [])

    def getCountry(self):
        """
        Two-letter ISO code representing the country of the card (as accurately as we can determine it). You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        return self.base.get("country", [])

    def getExpMonth(self):
        """
        Card's expiration month.
        """
        return self.base.get("exp_month", [])

    def getExpYear(self):
        """
        Card's expiration year. (yyyy).
        """
        return self.base.get("exp_year", [])

    def getFingerprint(self):
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example.
        """
        return self.base.get("fingerprint", [])

    def getLast4(self):
        """
        Last 4 digits of the card's number.
        """
        return self.base.get("last4", [])

    def getName(self):
        """
        Cardholder name
        """
        return self.base.get("name", [])

    def getObject(self):
        """
        Value is always "card"
        """
        return self.base.get("object", [])

    def getType(self):
        """
        Credit card type (visa/mastercard)
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

