# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveInvoice
# Retrieves invoice details using the invoice id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeInvoice import StripeInvoice

import json

class RetrieveInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Invoices/RetrieveInvoice')


    def new_input_set(self):
        return RetrieveInvoiceInputSet()

    def _make_result_set(self, result, path):
        return RetrieveInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveInvoiceChoreographyExecution(session, exec_id, path)

class RetrieveInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_InvoiceID(self, value):
        """
        Set the value of the InvoiceID input for this Choreo. ((required, string) The unique identifier of the invoice you want to retrieve)
        """
        InputSet._set_input(self, 'InvoiceID', value)

class RetrieveInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveInvoice Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getInvoice(self):
        """
        A reference to the Stripe Invoice object
        """
        return StripeInvoice(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveInvoiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveInvoiceResultSet(response, path)
