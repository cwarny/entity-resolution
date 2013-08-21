# -*- coding: utf-8 -*-

###############################################################################
#
# MakeIndividualPayment
# Retrieves the available balance for a PayPal account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MakeIndividualPayment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MakeIndividualPayment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Merchant/MakeIndividualPayment')


    def new_input_set(self):
        return MakeIndividualPaymentInputSet()

    def _make_result_set(self, result, path):
        return MakeIndividualPaymentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MakeIndividualPaymentChoreographyExecution(session, exec_id, path)

class MakeIndividualPaymentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MakeIndividualPayment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((optional, string) The currency code associated with the PaymentAmount. Defaults to "USD".)
        """
        InputSet._set_input(self, 'CurrencyCode', value)
    def set_EmailAddress(self, value):
        """
        Set the value of the EmailAddress input for this Choreo. ((required, string) The email address used to identify the recipient of the payment.)
        """
        InputSet._set_input(self, 'EmailAddress', value)
    def set_EmailSubject(self, value):
        """
        Set the value of the EmailSubject input for this Choreo. ((optional, string) The subject line of the email that PayPal sends when the transaction is completed. Character length and limitations: 255 single-byte alphanumeric characters.)
        """
        InputSet._set_input(self, 'EmailSubject', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_PaymentAmount(self, value):
        """
        Set the value of the PaymentAmount input for this Choreo. ((required, decimal) The amount to be paid.)
        """
        InputSet._set_input(self, 'PaymentAmount', value)
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((required, string) The API Signature provided by PayPal.)
        """
        InputSet._set_input(self, 'Signature', value)
    def set_UseSandbox(self, value):
        """
        Set the value of the UseSandbox input for this Choreo. ((optional, boolean) Set to 1 to indicate that you're testing against the PayPal sandbox instead of production. Set to 0 (the default) when moving to production.)
        """
        InputSet._set_input(self, 'UseSandbox', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The API Username provided by PayPal.)
        """
        InputSet._set_input(self, 'Username', value)

class MakeIndividualPaymentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MakeIndividualPayment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Acknowledged(self):
        """
        Retrieve the value for the "Acknowledged" output from this Choreo execution. ((string) Indicates the status of the request. Should contain "Sucess" or "Failure".)
        """
        return self._output.get('Acknowledged', None)
    def get_CorrelationId(self):
        """
        Retrieve the value for the "CorrelationId" output from this Choreo execution. ((string) A unique id returned by PayPal for this payment.)
        """
        return self._output.get('CorrelationId', None)
    def get_ErrorMessage(self):
        """
        Retrieve the value for the "ErrorMessage" output from this Choreo execution. ((string) This will contain any error message returned by PayPal during this operation.)
        """
        return self._output.get('ErrorMessage', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The full response from PayPal formatted in name/value pairs.)
        """
        return self._output.get('Response', None)
    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) The timestamp associated with the payment request.)
        """
        return self._output.get('Timestamp', None)

class MakeIndividualPaymentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MakeIndividualPaymentResultSet(response, path)
