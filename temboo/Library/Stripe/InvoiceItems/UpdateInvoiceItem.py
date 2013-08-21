# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateInvoiceItem
# Updates the amount or description of an existing invoice item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeInvoiceItem import StripeInvoiceItem

import json

class UpdateInvoiceItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateInvoiceItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/InvoiceItems/UpdateInvoiceItem')


    def new_input_set(self):
        return UpdateInvoiceItemInputSet()

    def _make_result_set(self, result, path):
        return UpdateInvoiceItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateInvoiceItemChoreographyExecution(session, exec_id, path)

class UpdateInvoiceItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateInvoiceItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, integer) The amount in cents of the charge to be included in the customer's next invoice)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_Currency(self, value):
        """
        Set the value of the Currency input for this Choreo. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        InputSet._set_input(self, 'Currency', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be included with the invoice item)
        """
        InputSet._set_input(self, 'Description', value)
    def set_InvoiceItemID(self, value):
        """
        Set the value of the InvoiceItemID input for this Choreo. ((required, string) The unique identifier of the invoice item you want to update)
        """
        InputSet._set_input(self, 'InvoiceItemID', value)

class UpdateInvoiceItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateInvoiceItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getInvoiceItem(self):
        """
        Sometimes you want to add a charge or credit to a customer but only actually charge the customer's card at the end of a regular billing cycle. This is useful for combining several charges to minimize per-transaction fees or having Stripe tabulate your usage-based billing totals.
        """
        return StripeInvoiceItem(self.getJSONFromString(self._output.get('Response', [])))

class UpdateInvoiceItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateInvoiceItemResultSet(response, path)
