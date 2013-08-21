# -*- coding: utf-8 -*-

###############################################################################
#
# ConvertCurrency
# Converts a payment amount from one currency to another.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ConvertCurrency(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ConvertCurrency Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/AdaptivePayments/ConvertCurrency')


    def new_input_set(self):
        return ConvertCurrencyInputSet()

    def _make_result_set(self, result, path):
        return ConvertCurrencyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertCurrencyChoreographyExecution(session, exec_id, path)

class ConvertCurrencyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ConvertCurrency
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Amount(self, value):
        """
        Set the value of the Amount input for this Choreo. ((required, decimal) The amount that should be converted to a new currency.)
        """
        InputSet._set_input(self, 'Amount', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) Your PayPal AppID (or the default AppID for the PayPal sandbox).)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_ConvertToCurrency(self, value):
        """
        Set the value of the ConvertToCurrency input for this Choreo. ((required, string) The currency code that you want to convert to (i.e. GBP).)
        """
        InputSet._set_input(self, 'ConvertToCurrency', value)
    def set_CurrencyCode(self, value):
        """
        Set the value of the CurrencyCode input for this Choreo. ((required, string) The currency code that you want to convert. (i.e. USD).)
        """
        InputSet._set_input(self, 'CurrencyCode', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The API Password provided by PayPal.)
        """
        InputSet._set_input(self, 'Password', value)
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

class ConvertCurrencyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ConvertCurrency Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from PayPal.)
        """
        return self._output.get('Response', None)

class ConvertCurrencyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertCurrencyResultSet(response, path)
