# -*- coding: utf-8 -*-

###############################################################################
#
# CreateRepo
# Creates a new repository for the authenticated user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateRepo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateRepo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Repos/CreateRepo')


    def new_input_set(self):
        return CreateRepoInputSet()

    def _make_result_set(self, result, path):
        return CreateRepoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateRepoChoreographyExecution(session, exec_id, path)

class CreateRepoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateRepo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) A text description for the repo.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_HasDownloads(self, value):
        """
        Set the value of the HasDownloads input for this Choreo. ((optional, boolean) Se to "true" to enable downloads for this repository. Defaults to "true".)
        """
        InputSet._set_input(self, 'HasDownloads', value)
    def set_HasIssues(self, value):
        """
        Set the value of the HasIssues input for this Choreo. ((optional, boolean) Set to "true" to enable issues for this repository. Defaults to "true.")
        """
        InputSet._set_input(self, 'HasIssues', value)
    def set_HasWiki(self, value):
        """
        Set the value of the HasWiki input for this Choreo. ((optional, boolean) Set to "true" to enable the wiki for this repository. Defaults to "true".)
        """
        InputSet._set_input(self, 'HasWiki', value)
    def set_Homepage(self, value):
        """
        Set the value of the Homepage input for this Choreo. ((optional, string) A homepage link.)
        """
        InputSet._set_input(self, 'Homepage', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the repo being created.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Private(self, value):
        """
        Set the value of the Private input for this Choreo. ((optional, boolean) A flag indicating the the repo is private or public. Set to "true" to create a private repository. Defaults to "false".)
        """
        InputSet._set_input(self, 'Private', value)
    def set_TeamID(self, value):
        """
        Set the value of the TeamID input for this Choreo. ((optional, integer) The id of the team that will be granted access to this repository. Only valid when creating a repo in an organization.)
        """
        InputSet._set_input(self, 'TeamID', value)

class CreateRepoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateRepo Choreo.
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

class CreateRepoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateRepoResultSet(response, path)
