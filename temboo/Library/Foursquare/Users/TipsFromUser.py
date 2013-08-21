# -*- coding: utf-8 -*-

###############################################################################
#
# TipsFromUser
# Returns tips from a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareList import FoursquareList
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class TipsFromUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TipsFromUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Users/TipsFromUser')


    def new_input_set(self):
        return TipsFromUserInputSet()

    def _make_result_set(self, result, path):
        return TipsFromUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TipsFromUserChoreographyExecution(session, exec_id, path)

class TipsFromUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TipsFromUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude point of the user's location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 500.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) The longitude point of the user's location.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The FourSquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) Used to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Enter: recent, nearby, or popular. NEARBY requires geolat and geolong to be provided.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Identity of the user to get tips for. Defaults to "self" to get lists of the acting user.)
        """
        InputSet._set_input(self, 'UserID', value)

class TipsFromUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TipsFromUser Choreo.
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

    def getList(self):
        """
        Get tips for this user
        """
        return FoursquareList(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("list", []))

class TipsFromUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TipsFromUserResultSet(response, path)
