# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCustomer
# Retrieves the details of an existing customer record.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeCustomer import StripeCustomer

import json

class RetrieveCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Customers/RetrieveCustomer')


    def new_input_set(self):
        return RetrieveCustomerInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCustomerChoreographyExecution(session, exec_id, path)

class RetrieveCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to retrieve)
        """
        InputSet._set_input(self, 'CustomerID', value)

class RetrieveCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCustomer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getCustomer(self):
        """
        Customer objects allow you to perform recurring charges and track multiple charges that are associated with the same customer. The API allows you to create, delete, and update your customers. You can retrieve individual customers as well as a list of all your customers.
        """
        return StripeCustomer(self.getJSONFromString(self._output.get('Response', [])))

class RetrieveCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCustomerResultSet(response, path)
