# -*- coding: utf-8 -*-

###############################################################################
#
# MusicArtists
# Retrieves a list of NPR music artists and corresponding IDs. Also used to look up the IDs of specific NPR music artists by specifying them as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MusicArtists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MusicArtists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/MusicArtists')


    def new_input_set(self):
        return MusicArtistsInputSet()

    def _make_result_set(self, result, path):
        return MusicArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MusicArtistsChoreographyExecution(session, exec_id, path)

class MusicArtistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MusicArtists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_MusicArtist(self, value):
        """
        Set the value of the MusicArtist input for this Choreo. ((optional, string) The specific name or an NPR music artist to return. Multiple names can be specified separated by commas (i.e. Thom Yorke,Yo La Tengo). Music artist IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'MusicArtist', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying MusicArtist, only xml is returned.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_StoryCountAll(self, value):
        """
        Set the value of the StoryCountAll input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories.)
        """
        InputSet._set_input(self, 'StoryCountAll', value)
    def set_StoryCountMonth(self, value):
        """
        Set the value of the StoryCountMonth input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published in the last month.)
        """
        InputSet._set_input(self, 'StoryCountMonth', value)
    def set_StoryCountToday(self, value):
        """
        Set the value of the StoryCountToday input for this Choreo. ((optional, integer) Returns only items with at least this number of associated stories published today.)
        """
        InputSet._set_input(self, 'StoryCountToday', value)

class MusicArtistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MusicArtists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the music artist. This is only returned when the MusicArtist input is specified. When multiple artist names are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class MusicArtistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MusicArtistsResultSet(response, path)
