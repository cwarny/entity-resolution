# -*- coding: utf-8 -*-

###############################################################################
#
# RecentCheckins
# Returns a list of recent friends' check-ins.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification
from temboo.outputs.Foursquare.FoursquareRecent import FoursquareRecent

import json

class RecentCheckins(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RecentCheckins Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/RecentCheckins')


    def new_input_set(self):
        return RecentCheckinsInputSet()

    def _make_result_set(self, result, path):
        return RecentCheckinsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecentCheckinsChoreographyExecution(session, exec_id, path)

class RecentCheckinsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RecentCheckins
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AfterTimeStamp(self, value):
        """
        Set the value of the AfterTimeStamp input for this Choreo. ((optional, integer) Seconds after which to look for check-ins, e.g. for looking for new check-ins since the last fetch.)
        """
        InputSet._set_input(self, 'AfterTimeStamp', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude point of the user's location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to return, up to 100.)
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
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class RecentCheckinsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RecentCheckins Choreo.
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

    def getRecent(self):
        """
        Get recent checkins
        """
        return [FoursquareRecent(le) for le in self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("recent", [])]


class RecentCheckinsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecentCheckinsResultSet(response, path)
