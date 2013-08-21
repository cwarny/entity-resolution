# -*- coding: utf-8 -*-

###############################################################################
#
# GetEvents
# Retrieves a list of upcoming events for this artist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetEvents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEvents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Artist/GetEvents')


    def new_input_set(self):
        return GetEventsInputSet()

    def _make_result_set(self, result, path):
        return GetEventsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEventsChoreographyExecution(session, exec_id, path)

class GetEventsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEvents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Artist(self, value):
        """
        Set the value of the Artist input for this Choreo. ((conditional, string) The artist name. Required unless providing MbID.)
        """
        InputSet._set_input(self, 'Artist', value)
    def set_AutoCorrect(self, value):
        """
        Set the value of the AutoCorrect input for this Choreo. ((optional, boolean) Transform misspelled artist names into correct artist names. The corrected artist name will be returned in the response. Defaults to 0.)
        """
        InputSet._set_input(self, 'AutoCorrect', value)
    def set_FestivalsOnly(self, value):
        """
        Set the value of the FestivalsOnly input for this Choreo. ((optional, boolean) Whether only festivals should be returned, or all events. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'FestivalsOnly', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to fetch per page. Defaults to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the artist. Required unless providing Artist.)
        """
        InputSet._set_input(self, 'MbID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to fetch. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)

class GetEventsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEvents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetEventsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEventsResultSet(response, path)
