# -*- coding: utf-8 -*-

###############################################################################
#
# CompareUsers
# Retrieves a Tasteometer score from two user inputs, along with a list of shared artists.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CompareUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompareUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Tasteometer/CompareUsers')


    def new_input_set(self):
        return CompareUsersInputSet()

    def _make_result_set(self, result, path):
        return CompareUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareUsersChoreographyExecution(session, exec_id, path)

class CompareUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompareUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) How many shared artists to display. Defaults to 5.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_User1(self, value):
        """
        Set the value of the User1 input for this Choreo. ((string) The first user to compare.)
        """
        InputSet._set_input(self, 'User1', value)
    def set_User2(self, value):
        """
        Set the value of the User2 input for this Choreo. ((string) The second user to compare.)
        """
        InputSet._set_input(self, 'User2', value)

class CompareUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompareUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class CompareUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompareUsersResultSet(response, path)
