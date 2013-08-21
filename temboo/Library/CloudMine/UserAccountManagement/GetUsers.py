# -*- coding: utf-8 -*-

###############################################################################
#
# GetUsers
# Retrieves a list of all users that have been created for your application.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/UserAccountManagement/GetUsers')


    def new_input_set(self):
        return GetUsersInputSet()

    def _make_result_set(self, result, path):
        return GetUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUsersChoreographyExecution(session, exec_id, path)

class GetUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)

class GetUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class GetUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUsersResultSet(response, path)
