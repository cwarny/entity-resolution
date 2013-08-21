# -*- coding: utf-8 -*-

###############################################################################
#
# CreateUser
# Creates a new user in an enterprise.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Users/CreateUser')


    def new_input_set(self):
        return CreateUserInputSet()

    def _make_result_set(self, result, path):
        return CreateUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateUserChoreographyExecution(session, exec_id, path)

class CreateUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UserObject(self, value):
        """
        Set the value of the UserObject input for this Choreo. ((required, json) A JSON object representing the new user. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'UserObject', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)

class CreateUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class CreateUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateUserResultSet(response, path)
