# -*- coding: utf-8 -*-

###############################################################################
#
# User
# Retrieves information about the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Facebook.FacebookUser import FacebookUser

import json

class User(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the User Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/User')


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
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class UserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the User Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getUser(self):
        """
        Get the details for the user
        """
        return FacebookUser(self.getJSONFromString(self._output.get('Response', [])))

class UserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UserResultSet(response, path)
