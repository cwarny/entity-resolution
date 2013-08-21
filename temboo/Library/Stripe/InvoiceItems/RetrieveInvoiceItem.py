# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveInvoiceItem
# Retrieves invoice items with a specified id.
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

class RetrieveInvoiceItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveInvoiceItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/InvoiceItems/RetrieveInvoiceItem')


    def new_input_set(self):
        return RetrieveInvoiceItemInputSet()

    def _make_result_set(self, result, path):
        return RetrieveInvoiceItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveInvoiceItemChoreographyExecution(session, exec_id, path)

class RetrieveInvoiceItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveInvoiceItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The secret API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_InvoiceItemID(self, value):
        """
        Set the value of the InvoiceItemID input for this Choreo. ((required, string) The unique identifier of the invoice item you want to retrieve)
        """
        InputSet._set_input(self, 'InvoiceItemID', value)

class RetrieveInvoiceItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveInvoiceItem Choreo.
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

class RetrieveInvoiceItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveInvoiceItemResultSet(response, path)
