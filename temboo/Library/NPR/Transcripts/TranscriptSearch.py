# -*- coding: utf-8 -*-

###############################################################################
#
# TranscriptSearch
# Retrieves transcripts of NPR stories based on their unique story IDs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TranscriptSearch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TranscriptSearch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/Transcripts/TranscriptSearch')


    def new_input_set(self):
        return TranscriptSearchInputSet()

    def _make_result_set(self, result, path):
        return TranscriptSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TranscriptSearchChoreographyExecution(session, exec_id, path)

class TranscriptSearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TranscriptSearch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The story ID for which you want a transcript. You can find the story ID by first running an aprropriate StoryFinder Choreo.)
        """
        InputSet._set_input(self, 'ID', value)

class TranscriptSearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TranscriptSearch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class TranscriptSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TranscriptSearchResultSet(response, path)
