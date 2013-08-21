# -*- coding: utf-8 -*-

###############################################################################
#
# Like
# Allows the authenticated user to like or unlike a check-in.
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
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class Like(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Like Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/Like')


    def new_input_set(self):
        return LikeInputSet()

    def _make_result_set(self, result, path):
        return LikeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikeChoreographyExecution(session, exec_id, path)

class LikeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Like
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in to like or unlike.)
        """
        InputSet._set_input(self, 'CheckinID', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Set(self, value):
        """
        Set the value of the Set input for this Choreo. ((optional, boolean) Set to 1 (the default) to like this check-in. Set to 0 to undo a previous like.)
        """
        InputSet._set_input(self, 'Set', value)

class LikeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Like Choreo.
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
    def getNotifications(self):
        """
        Get the count of unread notifications for the authenticated user
        """
        return [FoursquareNotification(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("notifications", [])]

    def getLikes(self):
        """
        Get likes for this checkin
        """
        return FoursquareLikes(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("likes", []))

class LikeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikeResultSet(response, path)
