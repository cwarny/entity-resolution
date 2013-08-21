# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteAccessKey
# Deletes the access key associated with the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteAccessKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteAccessKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/DeleteAccessKey')


    def new_input_set(self):
        return DeleteAccessKeyInputSet()

    def _make_result_set(self, result, path):
        return DeleteAccessKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteAccessKeyChoreographyExecution(session, exec_id, path)

class DeleteAccessKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteAccessKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) An AWS Access Key ID with sufficient permissions to delete the specified AccessKeyId.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID associated with the AWS AccessKey ID with sufficient permissions to delete the AccessKeyId.)
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
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((conditional, string) Name of the user whose key you want to delete.  If you do not specify a user name, IAM determines the user name implicitly based on the AWS Access Key ID signing the request.)
        """
        InputSet._set_input(self, 'UserName', value)

class DeleteAccessKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteAccessKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class DeleteAccessKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteAccessKeyResultSet(response, path)
