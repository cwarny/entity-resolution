# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllCustomers
# Returns a list of all customers. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeCustomerList import StripeCustomerList

import json

class ListAllCustomers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllCustomers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Customers/ListAllCustomers')


    def new_input_set(self):
        return ListAllCustomersInputSet()

    def _make_result_set(self, result, path):
        return ListAllCustomersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllCustomersChoreographyExecution(session, exec_id, path)

class ListAllCustomersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllCustomers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The limit of customers to be returned. Can range from 1 to 100. Defaults to 10.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Stripe will return a list of customers starting at the specified offset. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)

class ListAllCustomersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllCustomers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getCustomerList(self):
        """
        A list of your customers
        """
        return StripeCustomerList(self.getJSONFromString(self._output.get('Response', [])))

class ListAllCustomersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllCustomersResultSet(response, path)
