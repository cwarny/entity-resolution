# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewReleases
# Retrieves a list of forthcoming releases based on a user's musical taste. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetNewReleases(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNewReleases Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LastFm/User/GetNewReleases')


    def new_input_set(self):
        return GetNewReleasesInputSet()

    def _make_result_set(self, result, path):
        return GetNewReleasesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewReleasesChoreographyExecution(session, exec_id, path)

class GetNewReleasesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNewReleases
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((string) Your Last.fm API Key.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_UserRecommendations(self, value):
        """
        Set the value of the UserRecommendations input for this Choreo. ((optional, boolean) If 1, the feed contains new releases based on Last.fm's artist recommendations for this user. Otherwise, it is based on their library.)
        """
        InputSet._set_input(self, 'UserRecommendations', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((string) The Last.fm username.)
        """
        InputSet._set_input(self, 'User', value)

class GetNewReleasesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNewReleases Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) The response from Last.fm.)
        """
        return self._output.get('Response', None)

class GetNewReleasesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewReleasesResultSet(response, path)
