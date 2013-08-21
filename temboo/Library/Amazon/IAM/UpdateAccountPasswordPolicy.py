# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountPasswordPolicy
# Updates the password policy settings for the account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccountPasswordPolicy(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountPasswordPolicy Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/IAM/UpdateAccountPasswordPolicy')


    def new_input_set(self):
        return UpdateAccountPasswordPolicyInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountPasswordPolicyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountPasswordPolicyChoreographyExecution(session, exec_id, path)

class UpdateAccountPasswordPolicyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountPasswordPolicy
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
    def set_AllowUsersToChangePassword(self, value):
        """
        Set the value of the AllowUsersToChangePassword input for this Choreo. ((optional, boolean) Determines whether users can set/change their own passwords. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'AllowUsersToChangePassword', value)
    def set_ExpirePasswords(self, value):
        """
        Set the value of the ExpirePasswords input for this Choreo. ((optional, boolean) Determines whether the passwords expire. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'ExpirePasswords', value)
    def set_MaxPasswordsAge(self, value):
        """
        Set the value of the MaxPasswordsAge input for this Choreo. ((optional, integer) Maximum age of the passwords before they expire.)
        """
        InputSet._set_input(self, 'MaxPasswordsAge', value)
    def set_MinimumPasswordLength(self, value):
        """
        Set the value of the MinimumPasswordLength input for this Choreo. ((optional, integer) Mininum length of the password. Defaults to none.)
        """
        InputSet._set_input(self, 'MinimumPasswordLength', value)
    def set_RequireLowercaseCharacters(self, value):
        """
        Set the value of the RequireLowercaseCharacters input for this Choreo. ((optional, boolean) Determines whether at least one lower-case character is required in the password. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'RequireLowercaseCharacters', value)
    def set_RequireNumbers(self, value):
        """
        Set the value of the RequireNumbers input for this Choreo. ((optional, boolean) Determines whether numbers are required in the password. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'RequireNumbers', value)
    def set_RequireSymbols(self, value):
        """
        Set the value of the RequireSymbols input for this Choreo. ((optional, boolean) Determines whether symbols are required in the password. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'RequireSymbols', value)
    def set_RequireUppercaseCharacters(self, value):
        """
        Set the value of the RequireUppercaseCharacters input for this Choreo. ((optional, boolean) Determines whether at least one upper-case character is required in the password. Valid values: "true" or "false" (the default).)
        """
        InputSet._set_input(self, 'RequireUppercaseCharacters', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class UpdateAccountPasswordPolicyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountPasswordPolicy Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class UpdateAccountPasswordPolicyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountPasswordPolicyResultSet(response, path)
