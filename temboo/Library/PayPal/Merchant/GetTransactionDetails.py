# -*- coding: utf-8 -*-

###############################################################################
#
# GetTransactionDetails
# Retrieves information about a specific transaction.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTransactionDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTransactionDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/PayPal/Merchant/GetTransactionDetails')


    def new_input_set(self):
        return GetTransactionDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetTransactionDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTransactionDetailsChoreographyExecution(session, exec_id, path)

class GetTransactionDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTransactionDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_TransactionID(self, value):
        """
        Set the value of the TransactionID input for this Choreo. ((required, string) The ID for the transaction you want to retrieve data for.)
        """
        InputSet._set_input(self, 'TransactionID', value)
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

class GetTransactionDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTransactionDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Response from PayPal formatted in name/value pairs.)
        """
        return self._output.get('Response', None)

class GetTransactionDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTransactionDetailsResultSet(response, path)
