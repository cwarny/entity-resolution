# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFolder
# Deletes a specified folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/DeleteFolder')


    def new_input_set(self):
        return DeleteFolderInputSet()

    def _make_result_set(self, result, path):
        return DeleteFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFolderChoreographyExecution(session, exec_id, path)

class DeleteFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder that you want to delete.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_Recursive(self, value):
        """
        Set the value of the Recursive input for this Choreo. ((optional, boolean) Whether or not to delete this folder if it has items within in. Defaults to true.)
        """
        InputSet._set_input(self, 'Recursive', value)


class DeleteFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class DeleteFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFolderResultSet(response, path)
