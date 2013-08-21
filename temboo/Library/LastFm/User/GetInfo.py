# -*- coding: utf-8 -*-

###############################################################################
#
# GetInfo
# Get information about a user profile.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetInfo')


    def new_input_set(self):
        return GetInfoInputSet()

    def _make_result_set(self, result, path):
        return GetInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInfoChoreographyExecution(session, exec_id, path)

class GetInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The user to fetch info for.)
        """
        InputSet._set_input(self, 'User', value)

class GetInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInfoResultSet(response, path)
