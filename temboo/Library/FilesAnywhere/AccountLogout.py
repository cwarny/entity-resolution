# -*- coding: utf-8 -*-

###############################################################################
#
# AccountLogout
# Logout a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AccountLogout(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AccountLogout Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/AccountLogout')


    def new_input_set(self):
        return AccountLogoutInputSet()

    def _make_result_set(self, result, path):
        return AccountLogoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountLogoutChoreographyExecution(session, exec_id, path)

class AccountLogoutInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AccountLogout
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The token retrieved from authentication.  Can be passed from the AccountLogin Choreo.)
        """
        InputSet._set_input(self, 'Token', value)

class AccountLogoutResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AccountLogout Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from FilesAnywhere.)
        """
        return self._output.get('Response', None)

class AccountLogoutChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountLogoutResultSet(response, path)
