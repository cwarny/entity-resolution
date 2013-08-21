# -*- coding: utf-8 -*-

###############################################################################
#
# GetTopTags
# Retrieves the top tags used by a user. 
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
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetTopTags')


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
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limit the number of tags returned. Defaults to 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The Last.fm username to fetch top tags for.)
        """
        InputSet._set_input(self, 'User', value)

class GetTopTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetTopTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetTopTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetTopTagsResultSet(response, path)
