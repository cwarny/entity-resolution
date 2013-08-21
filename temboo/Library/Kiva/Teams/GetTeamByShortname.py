# -*- coding: utf-8 -*-

###############################################################################
#
# GetTeamByShortname
# Returns detailed information about one or more teams, using team shortnames.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTeamByShortname(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTeamByShortname Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Kiva/Teams/GetTeamByShortname')


    def new_input_set(self):
        return GetTeamByShortnameInputSet()

    def _make_result_set(self, result, path):
        return GetTeamByShortnameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTeamByShortnameChoreographyExecution(session, exec_id, path)

class GetTeamByShortnameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTeamByShortname
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
    def set_TeamShortname(self, value):
        """
        Set the value of the TeamShortname input for this Choreo. ((required, string) The Team shortname for which to return details.)
        """
        InputSet._set_input(self, 'TeamShortname', value)

class GetTeamByShortnameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTeamByShortname Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Kiva.)
        """
        return self._output.get('Response', None)

class GetTeamByShortnameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTeamByShortnameResultSet(response, path)
