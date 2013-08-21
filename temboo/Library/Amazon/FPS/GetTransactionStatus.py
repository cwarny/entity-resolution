# -*- coding: utf-8 -*-

###############################################################################
#
# GetTransactionStatus
# Retrieves the status of a specified transaction.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTransactionStatus(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTransactionStatus Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/FPS/GetTransactionStatus')


    def new_input_set(self):
        return GetTransactionStatusInputSet()

    def _make_result_set(self, result, path):
        return GetTransactionStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTransactionStatusChoreographyExecution(session, exec_id, path)

class GetTransactionStatusInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTransactionStatus
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
    def set_TransactionId(self, value):
        """
        Set the value of the TransactionId input for this Choreo. ((required, string) The ID for the transaction status you want to retrieve.)
        """
        InputSet._set_input(self, 'TransactionId', value)

class GetTransactionStatusResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTransactionStatus Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Amazon.)
        """
        return self._output.get('Response', None)

class GetTransactionStatusChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTransactionStatusResultSet(response, path)
