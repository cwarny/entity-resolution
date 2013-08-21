# -*- coding: utf-8 -*-

###############################################################################
#
# ListCollaborators
# Retrieves a list of collaborators for the specified repository.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCollaborators(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCollaborators Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Collaborators/ListCollaborators')


    def new_input_set(self):
        return ListCollaboratorsInputSet()

    def _make_result_set(self, result, path):
        return ListCollaboratorsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCollaboratorsChoreographyExecution(session, exec_id, path)

class ListCollaboratorsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCollaborators
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo that has the collaborators to retrieve.)
        """
        InputSet._set_input(self, 'Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        InputSet._set_input(self, 'User', value)

class ListCollaboratorsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCollaborators Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)

class ListCollaboratorsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCollaboratorsResultSet(response, path)
