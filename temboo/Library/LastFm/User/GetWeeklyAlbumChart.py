# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeeklyAlbumChart
# Retrieves an album chart for a user profile, for a given date range.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWeeklyAlbumChart(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWeeklyAlbumChart Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetWeeklyAlbumChart')


    def new_input_set(self):
        return GetWeeklyAlbumChartInputSet()

    def _make_result_set(self, result, path):
        return GetWeeklyAlbumChartResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeeklyAlbumChartChoreographyExecution(session, exec_id, path)

class GetWeeklyAlbumChartInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWeeklyAlbumChart
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_EndTimestamp(self, value):
        """
        Set the value of the EndTimestamp input for this Choreo. ((optional, date) End timestamp at which the chart should end on, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        InputSet._set_input(self, 'EndTimestamp', value)
    def set_StartTimestamp(self, value):
        """
        Set the value of the StartTimestamp input for this Choreo. ((optional, date) Beginning timestamp at which the chart should start from, in UNIX timestamp format. This must be in the UTC time zone.)
        """
        InputSet._set_input(self, 'StartTimestamp', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The last.fm username to fetch the charts of.)
        """
        InputSet._set_input(self, 'User', value)

class GetWeeklyAlbumChartResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWeeklyAlbumChart Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetWeeklyAlbumChartChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeeklyAlbumChartResultSet(response, path)
