# -*- coding: utf-8 -*-

###############################################################################
#
# ChangePassword
# Allows the authenticating user to change their password.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ChangePassword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ChangePassword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/ChangePassword')


    def new_input_set(self):
        return ChangePasswordInputSet()

    def _make_result_set(self, result, path):
        return ChangePasswordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ChangePasswordChoreographyExecution(session, exec_id, path)

class ChangePasswordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ChangePassword
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The user's Access Key ID.)
        """
        InputSet._set_input(self, 'AWSAccessKeyId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The user's Secret Key ID.)
        """
        InputSet._set_input(self, 'AWSSecretKeyId', value)
    def set_NewPassword(self, value):
        """
        Set the value of the NewPassword input for this Choreo. ((required, string) The new password.)
        """
        InputSet._set_input(self, 'NewPassword', value)
    def set_OldPassword(self, value):
        """
        Set the value of the OldPassword input for this Choreo. ((required, string) The old password.)
        """
        InputSet._set_input(self, 'OldPassword', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ChangePasswordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ChangePassword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class ChangePasswordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ChangePasswordResultSet(response, path)
