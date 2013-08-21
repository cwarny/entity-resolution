# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateFolder
# Updates the information about a folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/UpdateFolder')


    def new_input_set(self):
        return UpdateFolderInputSet()

    def _make_result_set(self, result, path):
        return UpdateFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateFolderChoreographyExecution(session, exec_id, path)

class UpdateFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FolderObject(self, value):
        """
        Set the value of the FolderObject input for this Choreo. ((required, json) A JSON object representing the new folder information. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'FolderObject', value)
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
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder to update.)
        """
        InputSet._set_input(self, 'FolderID', value)

class UpdateFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateFolderResultSet(response, path)
