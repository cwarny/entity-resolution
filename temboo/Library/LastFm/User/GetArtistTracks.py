# -*- coding: utf-8 -*-

###############################################################################
#
# GetArtistTracks
# Retrieves a list of tracks by a given artist scrobbled by this user, including scrobble time.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetArtistTracks(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetArtistTracks Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetArtistTracks')


    def new_input_set(self):
        return GetArtistTracksInputSet()

    def _make_result_set(self, result, path):
        return GetArtistTracksResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetArtistTracksChoreographyExecution(session, exec_id, path)

class GetArtistTracksInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetArtistTracks
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((required, string) The artist name you are interested in.)
        """
        InputSet._set_input(self, 'Artist', value)
    def set_EndTimestamp(self, value):
        """
        Set the value of the EndTimestamp input for this Choreo. ((optional, date) A unix timestamp to end at.)
        """
        InputSet._set_input(self, 'EndTimestamp', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_StartTimestamp(self, value):
        """
        Set the value of the StartTimestamp input for this Choreo. ((optional, date) A unix timestamp to start at.)
        """
        InputSet._set_input(self, 'StartTimestamp', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The last.fm username to fetch the recent tracks of.)
        """
        InputSet._set_input(self, 'User', value)

class GetArtistTracksResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetArtistTracks Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetArtistTracksChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetArtistTracksResultSet(response, path)
