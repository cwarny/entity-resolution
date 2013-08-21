# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCustomer
# Updates a specified customer record.
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

class UpdateCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Customers/UpdateCustomer')


    def new_input_set(self):
        return UpdateCustomerInputSet()

    def _make_result_set(self, result, path):
        return UpdateCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCustomerChoreographyExecution(session, exec_id, path)

class UpdateCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccountBalance(self, value):
        """
        Set the value of the AccountBalance input for this Choreo. ((optional, integer) The amount in cents for the starting account balance. A negative amount represents a credit that will be used before charging the customer's card; a positive amount will be added to the next invoice.)
        """
        InputSet._set_input(self, 'AccountBalance', value)
    def set_Coupon(self, value):
        """
        Set the value of the Coupon input for this Choreo. ((optional, string) If you provide a coupon code, it can be specified here)
        """
        InputSet._set_input(self, 'Coupon', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The unique identifier of the customer you want to update)
        """
        InputSet._set_input(self, 'CustomerID', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The customer's email address)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((optional, string) The token associated with a set of credit card details.)
        """
        InputSet._set_input(self, 'Token', value)

class UpdateCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCustomer Choreo.
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

class UpdateCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateCustomerResultSet(response, path)
