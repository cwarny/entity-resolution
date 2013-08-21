# -*- coding: utf-8 -*-

###############################################################################
#
# Likes
# Returns friends and a total count of users who have liked a check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareLikes import FoursquareLikes
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta

import json

class Likes(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Likes Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/Likes')


    def new_input_set(self):
        return LikesInputSet()

    def _make_result_set(self, result, path):
        return LikesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikesChoreographyExecution(session, exec_id, path)

class LikesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Likes
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in to retrieve likes for.)
        """
        InputSet._set_input(self, 'CheckinID', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) Your Foursquare client ID, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) Your Foursquare client secret, obtained after registering at Foursquare. Required unless using the OauthToken input.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class LikesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Likes Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Foursquare. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getMeta(self):
        """
        Get the response status code
        """
        return FoursquareMeta(self.getJSONFromString(self._output.get('Response', [])).get("meta", []))
    def getLikes(self):
        """
        Get likes for the checkin
        """
        return FoursquareLikes(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("likes", []))

class LikesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikesResultSet(response, path)
