# -*- coding: utf-8 -*-

###############################################################################
#
# ListFiles
# Lists the files in all folders (or in a specified folder) and allows you to control the database columns returned in the result.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListFiles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListFiles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/ListFiles')


    def new_input_set(self):
        return ListFilesInputSet()

    def _make_result_set(self, result, path):
        return ListFilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFilesChoreographyExecution(session, exec_id, path)

class ListFilesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListFiles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) The database columns to return separated by commas. (i.e. downloads,lastdownload,filename,size, etc))
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileIDs(self, value):
        """
        Set the value of the FileIDs input for this Choreo. ((optional, integer) The id of the file to list. Multiple IDs can be entered separated by commas.)
        """
        InputSet._set_input(self, 'FileIDs', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((optional, string) The name of the file to list)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((optional, integer) The id of the folder that contains the file you want to list. Defaults to 'all'.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)

class ListFilesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListFiles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare formatted in commas separated values.)
        """
        return self._output.get('Response', None)

class ListFilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListFilesResultSet(response, path)
