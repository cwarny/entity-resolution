# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteAccountPasswordPolicy
# Deletes the password policy for the AWS account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteAccountPasswordPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteAccountPasswordPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/DeleteAccountPasswordPolicy')


    def new_input_set(self):
        return DeleteAccountPasswordPolicyInputSet()

    def _make_result_set(self, result, path):
        return DeleteAccountPasswordPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteAccountPasswordPolicyChoreographyExecution(session, exec_id, path)

class DeleteAccountPasswordPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteAccountPasswordPolicy
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
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class DeleteAccountPasswordPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteAccountPasswordPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteAccountPasswordPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteAccountPasswordPolicyResultSet(response, path)
