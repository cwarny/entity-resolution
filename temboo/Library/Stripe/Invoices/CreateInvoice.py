# -*- coding: utf-8 -*-

###############################################################################
#
# CreateInvoice
# Creates a new invoice for a customer.
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

class CreateInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Invoices/CreateInvoice')


    def new_input_set(self):
        return CreateInvoiceInputSet()

    def _make_result_set(self, result, path):
        return CreateInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateInvoiceChoreographyExecution(session, exec_id, path)

class CreateInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The id of the customer to create an invoice for.)
        """
        InputSet._set_input(self, 'CustomerID', value)

class CreateInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateInvoice Choreo.
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
        a reference to a Stripe Invoice object
        """
        return StripeInvoice(self.getJSONFromString(self._output.get('Response', [])))

class CreateInvoiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateInvoiceResultSet(response, path)
