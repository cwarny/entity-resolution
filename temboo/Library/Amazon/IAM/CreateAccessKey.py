# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAccessKey
# Creates a new AWS Secret Access Key and corresponding AWS Access Key ID for a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateAccessKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAccessKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/CreateAccessKey')


    def new_input_set(self):
        return CreateAccessKeyInputSet()

    def _make_result_set(self, result, path):
        return CreateAccessKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAccessKeyChoreographyExecution(session, exec_id, path)

class CreateAccessKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAccessKey
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
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((conditional, string) The user name that the new key will belong to.  If you do not specify a user name, IAM determines the user name implicitly based on the AWS Access Key ID signing the request. )
        """
        InputSet._set_input(self, 'UserName', value)

class CreateAccessKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAccessKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class CreateAccessKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAccessKeyResultSet(response, path)
