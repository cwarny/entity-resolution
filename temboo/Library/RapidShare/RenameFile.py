# -*- coding: utf-8 -*-

###############################################################################
#
# RenameFile
# Renames a file to something else.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RenameFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RenameFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/RenameFile')


    def new_input_set(self):
        return RenameFileInputSet()

    def _make_result_set(self, result, path):
        return RenameFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameFileChoreographyExecution(session, exec_id, path)

class RenameFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RenameFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileId(self, value):
        """
        Set the value of the FileId input for this Choreo. ((required, integer) The ID of the file to be renamed. Can be a commas separated list of ids.)
        """
        InputSet._set_input(self, 'FileId', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_NewFileName(self, value):
        """
        Set the value of the NewFileName input for this Choreo. ((required, string) The new file name.)
        """
        InputSet._set_input(self, 'NewFileName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)

class RenameFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RenameFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare. The ID of the newly created folder should be returned in the response upon a successful execution.)
        """
        return self._output.get('Response', None)

class RenameFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RenameFileResultSet(response, path)
