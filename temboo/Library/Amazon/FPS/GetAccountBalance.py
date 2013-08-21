# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccountBalance
# Retrieves the current balance of your account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAccountBalance(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccountBalance Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetAccountBalance')


    def new_input_set(self):
        return GetAccountBalanceInputSet()

    def _make_result_set(self, result, path):
        return GetAccountBalanceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountBalanceChoreographyExecution(session, exec_id, path)

class GetAccountBalanceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccountBalance
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_Endpoint(self, value):
        """
        Set the value of the Endpoint input for this Choreo. ((optional, string) The endpoint should be fps.sandbox.amazonaws.com when accessing the sandbox. Defaults to production setting:  fps.amazonaws.com.)
        """
        InputSet._set_input(self, 'Endpoint', value)

class GetAccountBalanceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccountBalance Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetAccountBalanceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountBalanceResultSet(response, path)
