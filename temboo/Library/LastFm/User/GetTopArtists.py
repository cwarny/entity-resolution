# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopArtists
# Retrieves the top artists listened to by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTopArtists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopArtists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetTopArtists')


    def new_input_set(self):
        return GetTopArtistsInputSet()

    def _make_result_set(self, result, path):
        return GetTopArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopArtistsChoreographyExecution(session, exec_id, path)

class GetTopArtistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopArtists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Period(self, value):
        """
        Set the value of the Period input for this Choreo. ((optional, string) The time period over which to retrieve top artists for. Valid values are: overall, 7day, 3month, 6month, 12month. Defaults to 'overall'.)
        """
        InputSet._set_input(self, 'Period', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The Last.fm username to fetch top artists for.)
        """
        InputSet._set_input(self, 'User', value)

class GetTopArtistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopArtists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTopArtistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopArtistsResultSet(response, path)
