# -*- coding: utf-8 -*-

###############################################################################
#
# VerifyPayPalPayment
# Verifies that a PayPal payment from the Adaptive Payments API has been successfully completed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class VerifyPayPalPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VerifyPayPalPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Payments/VerifyPayPalPayment')


    def new_input_set(self):
        return VerifyPayPalPaymentInputSet()

    def _make_result_set(self, result, path):
        return VerifyPayPalPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VerifyPayPalPaymentChoreographyExecution(session, exec_id, path)

class VerifyPayPalPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VerifyPayPalPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((conditional, string) Your PayPal AppID (or the default AppID for the PayPal sandbox: APP-80W284485P519543T). This is used to authenticate PayPal's Adaptive Payments API.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, string) The API Password provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProofOfPayment(self, value):
        """
        Set the value of the ProofOfPayment input for this Choreo. ((required, json) The proof of payment received from the client SDK. This can be a proof of payment received from the Adaptive Payment API or the REST API.)
        """
        InputSet._set_input(self, 'ProofOfPayment', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((conditional, string) The API Signature provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        InputSet._set_input(self, 'Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) The API Username provided by PayPal. This is used to authenticate PayPal's Adaptive Payments API.)
        """
        InputSet._set_input(self, 'Username', value)

class VerifyPayPalPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VerifyPayPalPayment Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal. This includes the full response from retrieving payment details from the AdaptivePayments API.)
        """
        return self._output.get('Response', None)
    def get_VerificationStatus(self):
        """
        Retrieve the value for the "VerificationStatus" output from this Choreo execution. ((string) The status of the payment verification. This will set to either "verified" or "unverified" depending on the status of the payment details.)
        """
        return self._output.get('VerificationStatus', None)

class VerifyPayPalPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VerifyPayPalPaymentResultSet(response, path)
