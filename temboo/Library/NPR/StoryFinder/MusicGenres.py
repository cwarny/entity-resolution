# -*- coding: utf-8 -*-

###############################################################################
#
# MusicGenres
# Retrieves a list of NPR music genres and corresponding IDs. Also used to look up the IDs of specific NPR music genres by specifying those as an optional parameter.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MusicGenres(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MusicGenres Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StoryFinder/MusicGenres')


    def new_input_set(self):
        return MusicGenresInputSet()

    def _make_result_set(self, result, path):
        return MusicGenresResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MusicGenresChoreographyExecution(session, exec_id, path)

class MusicGenresInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MusicGenres
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_MusicGenre(self, value):
        """
        Set the value of the MusicGenre input for this Choreo. ((optional, string) The specific music genre title to return. Multiple genre titles can be specified separated by commas (i.e. Blues,Classical). Genre IDs are returned when this input is used.)
        """
        InputSet._set_input(self, 'MusicGenre', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Set to json or xml (the default). Note that when specifying MusicGenre, only xml is returned.)
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

class MusicGenresResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MusicGenres Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Id(self):
        """
        Retrieve the value for the "Id" output from this Choreo execution. ((integer) The ID of the music genre. This is only returned when the MusicGenre input is specified. When multiple genres are specified, this will be a list of IDs separated by commas.)
        """
        return self._output.get('Id', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from NPR.)
        """
        return self._output.get('Response', None)

class MusicGenresChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MusicGenresResultSet(response, path)
