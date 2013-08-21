# -*- coding: utf-8 -*-

###############################################################################
#
# LookupPayment
# Retrieves a specific payment resource by ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LookupPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LookupPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Payments/LookupPayment')


    def new_input_set(self):
        return LookupPaymentInputSet()

    def _make_result_set(self, result, path):
        return LookupPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LookupPaymentChoreographyExecution(session, exec_id, path)

class LookupPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LookupPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved from PayPal. Required unless providing the ClientID and ClientSecret which can be used to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by PayPal. Required unless a valid Access Token is provided.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by PayPal. Required unless a valid Access Token is provided.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_PaymentID(self, value):
        """
        Set the value of the PaymentID input for this Choreo. ((required, string) The id of the payment to retrieve.)
        """
        InputSet._set_input(self, 'PaymentID', value)
    def set_Scope(self, value):
        """
        Set the value of the Scope input for this Choreo. ((optional, string) A space delimited list of resource URL endpoints that the token should have access for. This is only used when providing the ClientID and Client Secret in order to generate a new access token.)
        """
        InputSet._set_input(self, 'Scope', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)

class LookupPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LookupPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Currency(self):
        """
        Retrieve the value for the "Currency" output from this Choreo execution. ((string) The payment currency.)
        """
        return self._output.get('Currency', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) The new access token retrieved from PayPal when providing the Client ID and Client Secret.)
        """
        return self._output.get('NewAccessToken', None)
    def get_PaymentState(self):
        """
        Retrieve the value for the "PaymentState" output from this Choreo execution. ((string) The state of the payment.)
        """
        return self._output.get('PaymentState', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)
    def get_SaleState(self):
        """
        Retrieve the value for the "SaleState" output from this Choreo execution. ((string) The state of the sale.)
        """
        return self._output.get('SaleState', None)
    def get_Total(self):
        """
        Retrieve the value for the "Total" output from this Choreo execution. ((decimal) The total amount of the payment.)
        """
        return self._output.get('Total', None)

class LookupPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LookupPaymentResultSet(response, path)
