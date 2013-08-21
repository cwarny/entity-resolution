# -*- coding: utf-8 -*-

###############################################################################
#
# VerifyCreditCardPayment
# Verifies that a credit card payment from the PayPal REST API has been completed successfully.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class VerifyCreditCardPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VerifyCreditCardPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Payments/VerifyCreditCardPayment')


    def new_input_set(self):
        return VerifyCreditCardPaymentInputSet()

    def _make_result_set(self, result, path):
        return VerifyCreditCardPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VerifyCreditCardPaymentChoreographyExecution(session, exec_id, path)

class VerifyCreditCardPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VerifyCreditCardPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved from PayPal. Required unless providing the ClientID and ClientSecret which can be used to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by PayPal. This is used to authenticate PayPal's REST API.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by PayPal. This is used to authenticate PayPal's REST API.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_ProofOfPayment(self, value):
        """
        Set the value of the ProofOfPayment input for this Choreo. ((conditional, json) The proof of payment received from the client SDK. This can be a proof of payment received from the Adaptive Payment API or the REST API.)
        """
        InputSet._set_input(self, 'ProofOfPayment', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)

class VerifyCreditCardPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VerifyCreditCardPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_FailureDescription(self):
        """
        Retrieve the value for the "FailureDescription" output from this Choreo execution. ((json) When the payment details indicate that the payment status is not complete, this will contain a JSON dictionary of payment status descriptions.)
        """
        return self._output.get('FailureDescription', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal. This includes the full response from retrieving payment details from the Rest API.)
        """
        return self._output.get('Response', None)
    def get_VerificationStatus(self):
        """
        Retrieve the value for the "VerificationStatus" output from this Choreo execution. ((string) The status of the payment verification. This will set to either "verified" or "unverified" depending on the status of the payment details.)
        """
        return self._output.get('VerificationStatus', None)

class VerifyCreditCardPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VerifyCreditCardPaymentResultSet(response, path)
