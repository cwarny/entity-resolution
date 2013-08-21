# -*- coding: utf-8 -*-

###############################################################################
#
# MoveRealFolder
# Changes the parent ID of existing RealFolders, enabling the location of the folder to be moved within a RapidShare account file hierarchy.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MoveRealFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MoveRealFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/MoveRealFolder')


    def new_input_set(self):
        return MoveRealFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveRealFolderChoreographyExecution(session, exec_id, path)

class MoveRealFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MoveRealFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FolderId(self, value):
        """
        Set the value of the FolderId input for this Choreo. ((required, integer) The id of the folder(s) to be moved. Can be a commas separated list of ids.)
        """
        InputSet._set_input(self, 'FolderId', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_NewParent(self, value):
        """
        Set the value of the NewParent input for this Choreo. ((required, integer) Enter the ID of new parent folder)
        """
        InputSet._set_input(self, 'NewParent', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)

class MoveRealFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MoveRealFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare. The id of the newly created folder should be returned in the response upon a successful execution.)
        """
        return self._output.get('Response', None)

class MoveRealFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveRealFolderResultSet(response, path)
