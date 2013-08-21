# -*- coding: utf-8 -*-

###############################################################################
#
# AddRealFolder
# Creates a new folder in RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddRealFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddRealFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/AddRealFolder')


    def new_input_set(self):
        return AddRealFolderInputSet()

    def _make_result_set(self, result, path):
        return AddRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddRealFolderChoreographyExecution(session, exec_id, path)

class AddRealFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddRealFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) The name of the folder (Max character length is 250 bytes))
        """
        InputSet._set_input(self, 'Name', value)
    def set_Parent(self, value):
        """
        Set the value of the Parent input for this Choreo. ((optional, integer) The ID of the parent folder. Defaults to 0 for 'root'.)
        """
        InputSet._set_input(self, 'Parent', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)

class AddRealFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddRealFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare. The id of the newly created folder should be returned in the response upon a successful execution.)
        """
        return self._output.get('Response', None)

class AddRealFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddRealFolderResultSet(response, path)
