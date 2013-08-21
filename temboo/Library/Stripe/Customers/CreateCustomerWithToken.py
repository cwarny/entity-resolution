# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCustomerWithToken
# Creates a new customer record using a Stripe generated token that represents the customer's credit card information.
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

class CreateCustomerWithToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCustomerWithToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Customers/CreateCustomerWithToken')


    def new_input_set(self):
        return CreateCustomerWithTokenInputSet()

    def _make_result_set(self, result, path):
        return CreateCustomerWithTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCustomerWithTokenChoreographyExecution(session, exec_id, path)

class CreateCustomerWithTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCustomerWithToken
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the customer object)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((optional, string) The customer's email address)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Plan(self, value):
        """
        Set the value of the Plan input for this Choreo. ((optional, string) The unique identifier of the plan to subscribe the customer to)
        """
        InputSet._set_input(self, 'Plan', value)
    def set_Quantity(self, value):
        """
        Set the value of the Quantity input for this Choreo. ((optional, integer) The quantity you'd like to apply to the subscription you're creating. This parameter applies to the plan amount associated with the customer.)
        """
        InputSet._set_input(self, 'Quantity', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) The token associated with a set of credit card details)
        """
        InputSet._set_input(self, 'Token', value)
    def set_TrialEnd(self, value):
        """
        Set the value of the TrialEnd input for this Choreo. ((optional, date) Epoch timestamp in seconds for the end of the trial period. The customer won't be charged during the trial period. Timestamp should be in UTC.)
        """
        InputSet._set_input(self, 'TrialEnd', value)

class CreateCustomerWithTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCustomerWithToken Choreo.
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

class CreateCustomerWithTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCustomerWithTokenResultSet(response, path)
