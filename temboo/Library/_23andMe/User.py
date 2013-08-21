# -*- coding: utf-8 -*-

###############################################################################
#
# User
# Retrieves the user id, and a list of profiles including their ids and whether or not they are genotyped.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class User(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the User Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/23andMe/User')


    def new_input_set(self):
        return UserInputSet()

    def _make_result_set(self, result, path):
        return UserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UserChoreographyExecution(session, exec_id, path)

class UserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the User
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after completing the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_TestMode(self, value):
        """
        Set the value of the TestMode input for this Choreo. ((optional, boolean) A boolean flag indicating that the request should be made to the "demo" 23andMe endpoint for testing. Set to 1 for test mode. Defaults to 0.)
        """
        InputSet._set_input(self, 'TestMode', value)

class UserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the User Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from 23AndMe.)
        """
        return self._output.get('Response', None)

class UserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserResultSet(response, path)
