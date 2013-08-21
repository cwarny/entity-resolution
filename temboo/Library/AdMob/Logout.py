# -*- coding: utf-8 -*-

###############################################################################
#
# Logout
# Logout from AdMob service.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Logout(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Logout Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/AdMob/Logout')


    def new_input_set(self):
        return LogoutInputSet()

    def _make_result_set(self, result, path):
        return LogoutResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogoutChoreographyExecution(session, exec_id, path)

class LogoutInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Logout
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        InputSet._set_input(self, 'ClientKey', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((required, string) The security token returned by the Login Choreo.)
        """
        InputSet._set_input(self, 'Token', value)

class LogoutResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Logout Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from AdMob in XML format)
        """
        return self._output.get('Response', None)

class LogoutChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogoutResultSet(response, path)
