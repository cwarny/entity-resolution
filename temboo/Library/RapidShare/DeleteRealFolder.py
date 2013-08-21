# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteRealFolder
# Delete a folder(s) from a RapidShare account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteRealFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteRealFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/DeleteRealFolder')


    def new_input_set(self):
        return DeleteRealFolderInputSet()

    def _make_result_set(self, result, path):
        return DeleteRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteRealFolderChoreographyExecution(session, exec_id, path)

class DeleteRealFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteRealFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_RealFolder(self, value):
        """
        Set the value of the RealFolder input for this Choreo. ((required, integer) The id of the folder to delete. Can be a commas separated list of ids.)
        """
        InputSet._set_input(self, 'RealFolder', value)

class DeleteRealFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteRealFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare)
        """
        return self._output.get('Response', None)

class DeleteRealFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteRealFolderResultSet(response, path)
