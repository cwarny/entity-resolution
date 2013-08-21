# -*- coding: utf-8 -*-

###############################################################################
#
# CheckinDetails
# Returns details of a check-in.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Foursquare.FoursquareCheckin import FoursquareCheckin
from temboo.outputs.Foursquare.FoursquareMeta import FoursquareMeta
from temboo.outputs.Foursquare.FoursquareNotification import FoursquareNotification

import json

class CheckinDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CheckinDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/CheckinDetails')


    def new_input_set(self):
        return CheckinDetailsInputSet()

    def _make_result_set(self, result, path):
        return CheckinDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckinDetailsChoreographyExecution(session, exec_id, path)

class CheckinDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CheckinDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CheckinID(self, value):
        """
        Set the value of the CheckinID input for this Choreo. ((required, string) The ID of the check-in to retrieve additional information for.)
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
    def set_Signature(self, value):
        """
        Set the value of the Signature input for this Choreo. ((optional, string) When check-ins are sent to public feeds such as Twitter, foursquare appends a signature to them (s=XXXXXX). The same value can be used here.)
        """
        InputSet._set_input(self, 'Signature', value)

class CheckinDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CheckinDetails Choreo.
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

    def getCheckin(self):
        """
        Get information about this checkin
        """
        return FoursquareCheckin(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("checkin", []))

class CheckinDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CheckinDetailsResultSet(response, path)
