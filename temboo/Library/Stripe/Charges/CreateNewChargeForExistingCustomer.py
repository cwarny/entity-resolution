# -*- coding: utf-8 -*-

###############################################################################
#
# CreateNewChargeForExistingCustomer
# Creates a new charge object in order to charge a credit card for an existing customer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Stripe.StripeCharge import StripeCharge

import json

class CreateNewChargeForExistingCustomer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateNewChargeForExistingCustomer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Charges/CreateNewChargeForExistingCustomer')


    def new_input_set(self):
        return CreateNewChargeForExistingCustomerInputSet()

    def _make_result_set(self, result, path):
        return CreateNewChargeForExistingCustomerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewChargeForExistingCustomerChoreographyExecution(session, exec_id, path)

class CreateNewChargeForExistingCustomerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateNewChargeForExistingCustomer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Stripe)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, integer) The amount to charge a customer in cents)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_Currency(self, value):
        """
        Set the value of the Currency input for this Choreo. ((optional, string) 3-letter ISO code for currency. Defaults to 'usd' which is currently the only supported currency.)
        """
        InputSet._set_input(self, 'Currency', value)
    def set_CustomerID(self, value):
        """
        Set the value of the CustomerID input for this Choreo. ((required, string) The id for the customer to charge)
        """
        InputSet._set_input(self, 'CustomerID', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        InputSet._set_input(self, 'Description', value)

class CreateNewChargeForExistingCustomerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateNewChargeForExistingCustomer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Stripe)
        """
        return self._output.get('Response', None)
    def getCharge(self):
        """
        To charge a credit or a debit card, you create a new charge object. You can retrieve and refund individual charges as well as list all charges. Charges are identified by a unique random ID.
        """
        return StripeCharge(self.getJSONFromString(self._output.get('Response', [])))

class CreateNewChargeForExistingCustomerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewChargeForExistingCustomerResultSet(response, path)
