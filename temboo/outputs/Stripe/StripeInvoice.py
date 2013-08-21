# coding: utf-8

class StripeInvoice:
    """
      Invoices are statements of what a customer owes for a particular billing period, including subscriptions, invoice items, and any automatic proration adjustments if necessary. Once an invoice is created, payment is automatically attempted. Note that the payment, while automatic, does not happen exactly at the time of invoice creation. If you have configured webhooks, the invoice will wait until one hour after the last webhook is successfully sent (or the last webhook times out after failing). Any customer credit on the account is applied before determining how much is due for that invoice (the amount that will be actually charged). If the amount due for the invoice is less than 50 cents (the minimum for a charge), we add the amount to the customer's running account balance to be added to the next invoice. If this amount is negative, it will act as a credit to offset the next invoice. Note that the customer account balance does not include unpaid invoices; it only includes balances that need to be taken into account when calculating the amount due for the next invoice.

    """

    def __init__(self, base):
        if base:
            self.base = base
        else:
            self.base = {}

    def getAmountDue(self):
        """
        Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the amount_due may be 0. If there is a positive starting_balance for the invoice (the customer owes money), the amount_due will also take that into account. The charge that gets generated for the invoice will be for the amount specified in amount_due.
        """
        return self.base.get("amount_due", [])

    def getAttemptCount(self):
        """
        Number of automatic payment attempts made for this invoice. Does not include manual attempts to pay the invoice.
        """
        return self.base.get("attempt_count", [])

    def getAttempted(self):
        """
        Whether or not an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the invoice.created webhook, for example, so you might not want to display that invoice as unpaid to your users.
        """
        return self.base.get("attempted", [])

    def getCharge(self):
        """
        ID of the charge
        """
        return self.base.get("charge", [])

    def getClosed(self):
        """
        Whether or not the invoice is still trying to collect payment. An invoice is closed if it's either paid or it has been marked closed. A closed invoice will no longer attempt to collect payment.
        """
        return self.base.get("closed", [])

    def getCurrency(self):
        """
        (3-letter ISO currency code)
        """
        return self.base.get("currency", [])

    def getCustomer(self):
        """
        ID of the customer
        """
        return self.base.get("customer", [])

    def getDate(self):
        """
        timestamp
        """
        return self.base.get("date", [])

    def getEndingBalance(self):
        """
        Ending customer balance after attempting to pay invoice. If the invoice has not been attempted yet, this will be nu
        """
        return self.base.get("ending_balance", [])

    def getId(self):
        """
        ID of the Invoice
        """
        return self.base.get("id", [])

    def getLines(self):
        """
        """
        return StripeLines(self.base.get("lines", []))

    def getLivemode(self):
        """
        In livemode, credit card transactions are actually processed.  In testmode, transactions don't go through the credit card network.
        """
        return self.base.get("livemode", [])

    def getNextPaymentAttempt(self):
        """
        timestamp
        """
        return self.base.get("next_payment_attempt", [])

    def getObject(self):
        """
        Value is always "invoice"
        """
        return self.base.get("object", [])

    def getPaid(self):
        """
        Whether or not payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance.
        """
        return self.base.get("paid", [])

    def getPeriodEnd(self):
        """
        timestamp.  End of the usage period the invoice covers
        """
        return self.base.get("period_end", [])

    def getPeriodStart(self):
        """
        timestamp.  Start of the usage period the invoice covers
        """
        return self.base.get("period_start", [])

    def getStartingBalance(self):
        """
        Starting customer balance before attempting to pay invoice. If the invoice has not been attempted yet, this will be the current customer balance.
        """
        return self.base.get("starting_balance", [])

    def getSubtotal(self):
        """
        Total of all subscriptions, invoice items, and prorations on the invoice before any discount is applied
        """
        return self.base.get("subtotal", [])

    def getTotal(self):
        """
        Total after discount
        """
        return self.base.get("total", [])

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

from temboo.outputs.Stripe.StripeLines import StripeLines