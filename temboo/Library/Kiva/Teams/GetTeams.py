# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeams
# Returns detailed information about one or more lending teams.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTeams(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTeams Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Teams/GetTeams')


    def new_input_set(self):
        return GetTeamsInputSet()

    def _make_result_set(self, result, path):
        return GetTeamsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeamsChoreographyExecution(session, exec_id, path)

class GetTeamsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTeams
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) Your unique application ID, usually in reverse DNS notation.)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Output returned can be XML or JSON. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_TeamID(self, value):
        """
        Set the value of the TeamID input for this Choreo. ((required, string) A list of team IDs for which details are to be returned. Max list items: 20.)
        """
        InputSet._set_input(self, 'TeamID', value)

class GetTeamsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTeams Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetTeamsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTeamsResultSet(response, path)
