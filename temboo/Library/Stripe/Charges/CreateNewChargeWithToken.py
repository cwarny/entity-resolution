# -*- coding: utf-8 -*-

###############################################################################
#
# CreateNewChargeWithToken
# Charges a credit card by creating a new charge object using a card token that is associated with the credit card details.
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

class CreateNewChargeWithToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateNewChargeWithToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Stripe/Charges/CreateNewChargeWithToken')


    def new_input_set(self):
        return CreateNewChargeWithTokenInputSet()

    def _make_result_set(self, result, path):
        return CreateNewChargeWithTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateNewChargeWithTokenChoreographyExecution(session, exec_id, path)

class CreateNewChargeWithTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateNewChargeWithToken
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
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) An arbitrary string of text that will be associated with the charge as a description)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The token associated with a set of credit card details. This can be generated with the CreateCardToken Choreo.)
        """
        InputSet._set_input(self, 'Token', value)

class CreateNewChargeWithTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateNewChargeWithToken Choreo.
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

class CreateNewChargeWithTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateNewChargeWithTokenResultSet(response, path)
