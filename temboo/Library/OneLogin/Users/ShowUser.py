# -*- coding: utf-8 -*-

###############################################################################
#
# ShowUser
# Retrieves information for a single user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShowUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/OneLogin/Users/ShowUser')


    def new_input_set(self):
        return ShowUserInputSet()

    def _make_result_set(self, result, path):
        return ShowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowUserChoreographyExecution(session, exec_id, path)

class ShowUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by OneLogin.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The id the user you want to return.)
        """
        InputSet._set_input(self, 'ID', value)

class ShowUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from OneLogin.)
        """
        return self._output.get('Response', None)

class ShowUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowUserResultSet(response, path)
