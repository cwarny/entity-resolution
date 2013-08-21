# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccessKey
# Changes the status of the specified access key from Active to Inactive, or vice versa. This action can be used to disable a user's key as part of a key rotation workflow.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccessKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccessKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/UpdateAccessKey')


    def new_input_set(self):
        return UpdateAccessKeyInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccessKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccessKeyChoreographyExecution(session, exec_id, path)

class UpdateAccessKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccessKey
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
    def set_AccessKeyId(self, value):
        """
        Set the value of the AccessKeyId input for this Choreo. ((conditional, string) The Access Key ID for the Access Key ID and Secret Access Key you want to delete.)
        """
        InputSet._set_input(self, 'AccessKeyId', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((required, string) The status you want to assign to the Secret Access Key. Active means the key can be used for API calls to AWS, while Inactive means the key cannot be used.)
        """
        InputSet._set_input(self, 'Status', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((conditional, string) Name of the user whose key you want to update.  If the UserName field is not specified, the UserName is determined implicitly based on the AWS Access Key ID used to sign the request.)
        """
        InputSet._set_input(self, 'UserName', value)

class UpdateAccessKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccessKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateAccessKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccessKeyResultSet(response, path)
