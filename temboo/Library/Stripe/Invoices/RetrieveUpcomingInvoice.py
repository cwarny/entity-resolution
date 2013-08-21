# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveUpcomingInvoice
# Retrieves a customer's upcoming invoice.
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

class RetrieveUpcomingInvoice(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveUpcomingInvoice Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Invoices/RetrieveUpcomingInvoice')


    def new_input_set(self):
        return RetrieveUpcomingInvoiceInputSet()

    def _make_result_set(self, result, path):
        return RetrieveUpcomingInvoiceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveUpcomingInvoiceChoreographyExecution(session, exec_id, path)

class RetrieveUpcomingInvoiceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveUpcomingInvoice
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer whose upcoming invoice to return)
        """
        InputSet._set_input(self, 'CustomerID', value)

class RetrieveUpcomingInvoiceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveUpcomingInvoice Choreo.
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

class RetrieveUpcomingInvoiceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveUpcomingInvoiceResultSet(response, path)
