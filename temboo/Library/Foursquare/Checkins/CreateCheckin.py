# -*- coding: utf-8 -*-

###############################################################################
#
# CreateCheckin
# Allows you to create a check-in with Foursquare.
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

class CreateCheckin(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateCheckin Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Checkins/CreateCheckin')


    def new_input_set(self):
        return CreateCheckinInputSet()

    def _make_result_set(self, result, path):
        return CreateCheckinResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCheckinChoreographyExecution(session, exec_id, path)

class CreateCheckinInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateCheckin
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccuracyOfCoordinates(self, value):
        """
        Set the value of the AccuracyOfCoordinates input for this Choreo. ((optional, integer) Accuracy of the user's latitude and longitude, in meters.)
        """
        InputSet._set_input(self, 'AccuracyOfCoordinates', value)
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Vertical accuracy of the user's location, in meters.)
        """
        InputSet._set_input(self, 'AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters.)
        """
        InputSet._set_input(self, 'Altitude', value)
    def set_Broadcast(self, value):
        """
        Set the value of the Broadcast input for this Choreo. ((optional, string) Who to broadcast this check-in to. Can be a comma-delimited list: private, public, facebook, twitter, or followers. Defaults to 'public'.)
        """
        InputSet._set_input(self, 'Broadcast', value)
    def set_EventID(self, value):
        """
        Set the value of the EventID input for this Choreo. ((optional, string) The event the user is checking in to. A venueId for a venue with this eventId must also be specified in the request.)
        """
        InputSet._set_input(self, 'EventID', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude point of the user's location.)
        """
        InputSet._set_input(self, 'Latitude', value)
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
    def set_Shout(self, value):
        """
        Set the value of the Shout input for this Choreo. ((optional, string) A message about your check-in. The maximum length of this field is 140 characters.)
        """
        InputSet._set_input(self, 'Shout', value)
    def set_VenueID(self, value):
        """
        Set the value of the VenueID input for this Choreo. ((required, string) The venue where the user is checking in. No venueid is needed if shouting or just providing a venue name.)
        """
        InputSet._set_input(self, 'VenueID', value)
    def set_Venue(self, value):
        """
        Set the value of the Venue input for this Choreo. ((optional, string) If you are not shouting, but you don't have a venue ID or prefer a 'venueless' checkin, pass the venue name as a string using this parameter.)
        """
        InputSet._set_input(self, 'Venue', value)

class CreateCheckinResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateCheckin Choreo.
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
        return [FoursquareNotification(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("notifications", [])]

    def getCheckin(self):
        """
        Get the checkin object
        """
        return FoursquareCheckin(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response").get("checkin", []))

class CreateCheckinChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCheckinResultSet(response, path)
