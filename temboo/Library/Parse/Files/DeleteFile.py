# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteFile
# Deletes a file stored on Parse.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Files/DeleteFile')


    def new_input_set(self):
        return DeleteFileInputSet()

    def _make_result_set(self, result, path):
        return DeleteFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFileChoreographyExecution(session, exec_id, path)

class DeleteFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, json) The name of the file to delete. Note that this is the name generated and returned by Parse after uploading the file.)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_MasterKey(self, value):
        """
        Set the value of the MasterKey input for this Choreo. ((required, string) The Master Key provided by Parse.)
        """
        InputSet._set_input(self, 'MasterKey', value)

class DeleteFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class DeleteFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFileResultSet(response, path)
