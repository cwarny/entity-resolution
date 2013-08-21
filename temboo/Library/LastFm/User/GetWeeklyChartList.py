# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeeklyChartList
# Retrieves a list of available charts for this user, expressed as date ranges which can be sent to the chart services.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWeeklyChartList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWeeklyChartList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetWeeklyChartList')


    def new_input_set(self):
        return GetWeeklyChartListInputSet()

    def _make_result_set(self, result, path):
        return GetWeeklyChartListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeeklyChartListChoreographyExecution(session, exec_id, path)

class GetWeeklyChartListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWeeklyChartList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The last.fm username to fetch the charts of.)
        """
        InputSet._set_input(self, 'User', value)

class GetWeeklyChartListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWeeklyChartList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetWeeklyChartListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeeklyChartListResultSet(response, path)
