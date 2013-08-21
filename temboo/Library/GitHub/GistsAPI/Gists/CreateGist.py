# -*- coding: utf-8 -*-

###############################################################################
#
# CreateGist
# Creates a gist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateGist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateGist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Gists/CreateGist')


    def new_input_set(self):
        return CreateGistInputSet()

    def _make_result_set(self, result, path):
        return CreateGistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateGistChoreographyExecution(session, exec_id, path)

class CreateGistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateGist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description for this gist.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((required, string) The file contents of the gist.)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The file name of the gist (i.e. myProject.py).)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_Public(self, value):
        """
        Set the value of the Public input for this Choreo. ((required, boolean) Indicates whether or not the gist is public or private.)
        """
        InputSet._set_input(self, 'Public', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The user who is creating the gist.)
        """
        InputSet._set_input(self, 'User', value)

class CreateGistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateGist Choreo.
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

class CreateGistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateGistResultSet(response, path)
