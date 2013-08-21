# -*- coding: utf-8 -*-

###############################################################################
#
# SearchSpecials
# Returns a list of specials near the current location.
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
from temboo.outputs.Foursquare.FoursquareSpecialsList import FoursquareSpecialsList

import json

class SearchSpecials(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchSpecials Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Specials/SearchSpecials')


    def new_input_set(self):
        return SearchSpecialsInputSet()

    def _make_result_set(self, result, path):
        return SearchSpecialsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchSpecialsChoreographyExecution(session, exec_id, path)

class SearchSpecialsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchSpecials
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccuracyOfCoordinates(self, value):
        """
        Set the value of the AccuracyOfCoordinates input for this Choreo. ((optional, integer) Accuracy of latitude and longitude, in meters.)
        """
        InputSet._set_input(self, 'AccuracyOfCoordinates', value)
    def set_AltitudeAccuracy(self, value):
        """
        Set the value of the AltitudeAccuracy input for this Choreo. ((optional, integer) Accuracy of the user's altitude, in meters.)
        """
        InputSet._set_input(self, 'AltitudeAccuracy', value)
    def set_Altitude(self, value):
        """
        Set the value of the Altitude input for this Choreo. ((optional, integer) Altitude of the user's location, in meters.)
        """
        InputSet._set_input(self, 'Altitude', value)
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
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) The latitude point of the user's location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to retun, up to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude point of the user's location.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Limit results to venues within this many meters of the specified location. Defaults to a city-wide area.)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class SearchSpecialsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchSpecials Choreo.
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

    def getSpecialsList(self):
        """
        Get specials offered by venues
        """
        return [FoursquareSpecialsList(le) for le in self.getJSONObject(self.getJSONObject(self.getJSONFromString(self._output.get('Response', [])), "response"), "specials").get("items", [])]


class SearchSpecialsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchSpecialsResultSet(response, path)
