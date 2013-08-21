# coding: utf-8

class StripeDispute:
    """
     A dispute occurs when a customer questions your charge with their bank or credit card company. When a customer disputes your charge, you're given the opportunity to respond to the dispute with evidence that shows the charge is legitimate. You can find more information about the dispute process in our

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAmount(self):
        """
        Disputed amount. Usually the amount of the charge, but can differ (usually because of currency fluctuation or because only part of the order is disputed).
        """
        return self.base.get("amount", [])

    def getCharge(self):
        """
        ID of the charge that was disputed
        """
        return self.base.get("charge", [])

    def getCreated(self):
        """
        Date dispute was opened
        """
        return self.base.get("created", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getEvidence(self):
        """
        Evidence that you have submitted to demonstrate the charge is legitimate (proof of delivery, IP addresses of logins, text of invoices, etc.). 1000 characters maximum.
        """
        return self.base.get("evidence", [])

    def getEvidenceDueBy(self):
        """
        Date by which evidence must be submitted in order to successfully challenge dispute.
        """
        return self.base.get("evidence_due_by", [])

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getObject(self):
        """
        always "dispute"
        """
        return self.base.get("object", [])

    def getReason(self):
        """
        Reason given by cardholder for dispute. Possible values are duplicate, fraudulent, subscription_canceled, product_unacceptable, product_not_received, unrecognized, credit_not_processed, general.
        """
        return self.base.get("reason", [])

    def getStatus(self):
        """
        Current status of dispute. Possible values are won, lost, needs_response, under_review.
        """
        return self.base.get("status", [])

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

