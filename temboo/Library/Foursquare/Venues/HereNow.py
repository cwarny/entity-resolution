# -*- coding: utf-8 -*-

###############################################################################
#
# HereNow
# Retrieves a count of how many people are at a given venue. For authenticated users, friends and friends-of-friends at the venue are also returned.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareHereNowList import FoursquareHereNowList
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class HereNow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HereNow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/HereNow')


    def new_input_set(self):
        return HereNowInputSet()

    def _make_result_set(self, result, path):
        return HereNowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HereNowChoreographyExecution(session, exec_id, path)

class HereNowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HereNow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimestamp(self, value):
        """
        Set the value of the AfterTimestamp input for this Choreo. ((optional, date) Retrieve the first results to follow this timestamp (an epoch timestamp in seconds).)
        """
        InputSet._set_input(self, 'AfterTimestamp', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return, up to 500.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) The Foursquare API Oauth token string.)
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
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The ID associated with the venue you want to retrieve details for.)
        """
        InputSet._set_input(self, 'VenueID', value)

class HereNowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HereNow Choreo.
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

    def getHereNowList(self):
        """
        Get the list of people here now
        """
        return FoursquareHereNowList(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("hereNow", []))

class HereNowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HereNowResultSet(response, path)
