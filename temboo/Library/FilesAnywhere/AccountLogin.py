# -*- coding: utf-8 -*-

###############################################################################
#
# AccountLogin
# Retrieves an authentication token from FilesAnywhere.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AccountLogin(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AccountLogin Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/AccountLogin')


    def new_input_set(self):
        return AccountLoginInputSet()

    def _make_result_set(self, result, path):
        return AccountLoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountLoginChoreographyExecution(session, exec_id, path)

class AccountLoginInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AccountLogin
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by FilesAnywhere.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AllowedIPList(self, value):
        """
        Set the value of the AllowedIPList input for this Choreo. ((optional, string) List of allowed IP addresses.  Multiple IP addresses can be separated by commas.)
        """
        InputSet._set_input(self, 'AllowedIPList', value)
    def set_ClientEncryptParam(self, value):
        """
        Set the value of the ClientEncryptParam input for this Choreo. ((optional, string) Used to return an encrypted password to use for subsequent logins.)
        """
        InputSet._set_input(self, 'ClientEncryptParam', value)
    def set_OrgID(self, value):
        """
        Set the value of the OrgID input for this Choreo. ((optional, integer) Defaults to 0 for a FilesAnywhere Web account.  Use 50 for a FilesAnywhere WebAdvanced account.)
        """
        InputSet._set_input(self, 'OrgID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your FilesAnywhere password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your FilesAnywhere username.)
        """
        InputSet._set_input(self, 'Username', value)

class AccountLoginResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AccountLogin Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FilesAnywhere.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) The token value parsed from the FilesAnywhere response.)
        """
        return self._output.get('Token', None)

class AccountLoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountLoginResultSet(response, path)
