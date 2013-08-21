# -*- coding: utf-8 -*-

###############################################################################
#
# CompareArtists
# Retrieves a Tasteometer score from two artist inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CompareArtists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompareArtists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Tasteometer/CompareArtists')


    def new_input_set(self):
        return CompareArtistsInputSet()

    def _make_result_set(self, result, path):
        return CompareArtistsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompareArtistsChoreographyExecution(session, exec_id, path)

class CompareArtistsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompareArtists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Artist1(self, value):
        """
        Set the value of the Artist1 input for this Choreo. ((string) The first artist to compare.)
        """
        InputSet._set_input(self, 'Artist1', value)
    def set_Artist2(self, value):
        """
        Set the value of the Artist2 input for this Choreo. ((string) The second artist to compare.)
        """
        InputSet._set_input(self, 'Artist2', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) How many shared artists to display. Defaults to 5.)
        """
        InputSet._set_input(self, 'Limit', value)

class CompareArtistsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompareArtists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class CompareArtistsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompareArtistsResultSet(response, path)
