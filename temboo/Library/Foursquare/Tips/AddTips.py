# -*- coding: utf-8 -*-

###############################################################################
#
# AddTips
# Allows you to add a new tip at a venue. 
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
from temboo.outputs.Foursquare.FoursquareTipDetails import FoursquareTipDetails

import json

class AddTips(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddTips Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Tips/AddTips')


    def new_input_set(self):
        return AddTipsInputSet()

    def _make_result_set(self, result, path):
        return AddTipsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddTipsChoreographyExecution(session, exec_id, path)

class AddTipsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddTips
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Broadcast(self, value):
        """
        Set the value of the Broadcast input for this Choreo. ((optional, string) Whether to broadcast this tip. Set to "twitter" if you want to send to twitter, "facebook" if you want to send to facebook, or "twitter,facebook" if you want to send to both.)
        """
        InputSet._set_input(self, 'Broadcast', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((required, string) Your Foursquare API Oauth token string.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text of the tip, up to 200 characters.)
        """
        InputSet._set_input(self, 'Text', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) A URL related to this tip.)
        """
        InputSet._set_input(self, 'URL', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The venue where you want to add this tip.)
        """
        InputSet._set_input(self, 'VenueID', value)

class AddTipsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddTips Choreo.
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

    def getTipDetails(self):
        """
        Get details for this tip
        """
        return FoursquareTipDetails(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("tip", []))

class AddTipsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddTipsResultSet(response, path)
