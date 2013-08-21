# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopTags
# Retrieves a list of the top tags for an album on Last.fm, ordered by popularity. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetTopTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetTopTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Album/GetTopTags')


    def new_input_set(self):
        return GetTopTagsInputSet()

    def _make_result_set(self, result, path):
        return GetTopTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetTopTagsChoreographyExecution(session, exec_id, path)

class GetTopTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetTopTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Album(self, value):
        """
        Set the value of the Album input for this Choreo. ((conditional, string) The album name. Required unless providing MbID.)
        """
        InputSet._set_input(self, 'Album', value)
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
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the album. Required unless providing the Album and Artist.)
        """
        InputSet._set_input(self, 'MbID', value)

class GetTopTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTopTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopTagsResultSet(response, path)
