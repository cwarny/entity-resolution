# -*- coding: utf-8 -*-

###############################################################################
#
# GetInfo
# Retrieves the metadata for an album on Last.fm using the album and artist name or a musicbrainz id.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/Album/GetInfo')


    def new_input_set(self):
        return GetInfoInputSet()

    def _make_result_set(self, result, path):
        return GetInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetInfoChoreographyExecution(session, exec_id, path)

class GetInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetInfo
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
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language to return the biography in, expressed as an ISO 639 alpha-2 code.)
        """
        InputSet._set_input(self, 'Language', value)
    def set_MbID(self, value):
        """
        Set the value of the MbID input for this Choreo. ((conditional, string) The musicbrainz id for the album. Required unless providing the Album and Artist.)
        """
        InputSet._set_input(self, 'MbID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) The username for the context of the request. If supplied, the user's playcount for this album is included in the response.)
        """
        InputSet._set_input(self, 'Username', value)

class GetInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetInfoResultSet(response, path)
