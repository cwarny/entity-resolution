# -*- coding: utf-8 -*-

###############################################################################
#
# GetTransaction
# Returns transactions for a specified subscription id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTransaction(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTransaction Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetTransaction')


    def new_input_set(self):
        return GetTransactionInputSet()

    def _make_result_set(self, result, path):
        return GetTransactionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTransactionChoreographyExecution(session, exec_id, path)

class GetTransactionInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTransaction
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
    def set_SubscriptionId(self, value):
        """
        Set the value of the SubscriptionId input for this Choreo. ((required, string) The ID for the subscription to retrieve the transactions for.)
        """
        InputSet._set_input(self, 'SubscriptionId', value)

class GetTransactionResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTransaction Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetTransactionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTransactionResultSet(response, path)
