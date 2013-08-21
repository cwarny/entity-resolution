# -*- coding: utf-8 -*-

###############################################################################
#
# GetGist
# Returns an individual gist with a given id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetGist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetGist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/GetGist')


    def new_input_set(self):
        return GetGistInputSet()

    def _make_result_set(self, result, path):
        return GetGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetGistChoreographyExecution(session, exec_id, path)

class GetGistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetGist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id for the gist you want to retrieve.)
        """
        InputSet._set_input(self, 'ID', value)

class GetGistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetGist Choreo.
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

class GetGistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetGistResultSet(response, path)
