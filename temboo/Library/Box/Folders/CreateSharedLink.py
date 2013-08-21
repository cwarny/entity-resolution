# -*- coding: utf-8 -*-

###############################################################################
#
# CreateSharedLink
# Creates a shared link for a particular folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateSharedLink(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateSharedLink Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/CreateSharedLink')


    def new_input_set(self):
        return CreateSharedLinkInputSet()

    def _make_result_set(self, result, path):
        return CreateSharedLinkResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSharedLinkChoreographyExecution(session, exec_id, path)

class CreateSharedLinkInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateSharedLink
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_SharedLink(self, value):
        """
        Set the value of the SharedLink input for this Choreo. ((required, json) A JSON object  representing the item’s shared link and associated permissions. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'SharedLink', value)
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
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder to get a shared link for.)
        """
        InputSet._set_input(self, 'FolderID', value)

class CreateSharedLinkResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateSharedLink Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class CreateSharedLinkChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSharedLinkResultSet(response, path)
