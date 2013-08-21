# -*- coding: utf-8 -*-

###############################################################################
#
# VenueDetail
# Obtain details about venues, including location, mayorship, tags, tips, specials and category.  Users who have authenticated via their oauth_token credential, also receive information about who is at the location being queried.
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
from temboo.outputs.Foursquare.FoursquareVenue import FoursquareVenue

import json

class VenueDetail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the VenueDetail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/VenueDetail')


    def new_input_set(self):
        return VenueDetailInputSet()

    def _make_result_set(self, result, path):
        return VenueDetailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return VenueDetailChoreographyExecution(session, exec_id, path)

class VenueDetailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the VenueDetail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        InputSet._set_input(self, 'OauthToken', value)
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

class VenueDetailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the VenueDetail Choreo.
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

    def getVenue(self):
        """
        Get venue details
        """
        return FoursquareVenue(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("venue", []))

class VenueDetailChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return VenueDetailResultSet(response, path)
