# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllInvoices
# Returns a list of all invoices or a list of invoices for a specified customer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeInvoiceList import StripeInvoiceList

import json

class ListAllInvoices(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllInvoices Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Invoices/ListAllInvoices')


    def new_input_set(self):
        return ListAllInvoicesInputSet()

    def _make_result_set(self, result, path):
        return ListAllInvoicesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllInvoicesChoreographyExecution(session, exec_id, path)

class ListAllInvoicesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllInvoices
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The limit of invoices to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((optional, string) The unique identifier of the customer whose invoice to return. If not specified, all invoices will be returned.)
        """
        InputSet._set_input(self, 'CustomerID', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Stripe will return a list of invoices starting at the specified offset. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)

class ListAllInvoicesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllInvoices Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getInvoiceList(self):
        """
        A list of invoices
        """
        return StripeInvoiceList(self.getJSONFromString(self._output.get('Response', [])))

class ListAllInvoicesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllInvoicesResultSet(response, path)
