# -*- coding: utf-8 -*-

###############################################################################
#
# Explore
# Returns a list of recommended venues near the current location.
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
from temboo.outputs.Foursquare.FoursquareRecommendations import FoursquareRecommendations

import json

class Explore(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Explore Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Foursquare/Venues/Explore')


    def new_input_set(self):
        return ExploreInputSet()

    def _make_result_set(self, result, path):
        return ExploreResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExploreChoreographyExecution(session, exec_id, path)

class ExploreInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Explore
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
    def set_Intent(self, value):
        """
        Set the value of the Intent input for this Choreo. ((optional, string) Limit results to venues when set to "specials".)
        """
        InputSet._set_input(self, 'Intent', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((conditional, decimal) The latitude point of the user's location. Required unless the Near parameter is provided.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Number of results to retun, up to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((conditional, decimal) The longitude point of the user's location. Required unless the Near parameter is provided.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Near(self, value):
        """
        Set the value of the Near input for this Choreo. ((conditional, string) A string naming a place in the world. If the near string is not geocodable, returns a failed_geocode error. Required unless provided Latitude and Longitude.)
        """
        InputSet._set_input(self, 'Near', value)
    def set_Novelty(self, value):
        """
        Set the value of the Novelty input for this Choreo. ((optional, string) Pass new or old to limit results to places the acting user hasn't been or has been, respectively. Omitting this parameter returns a mixture of both new and old.)
        """
        InputSet._set_input(self, 'Novelty', value)
    def set_OauthToken(self, value):
        """
        Set the value of the OauthToken input for this Choreo. ((conditional, string) The Foursquare API Oauth token string. Required unless specifying the ClientID and ClientSecret.)
        """
        InputSet._set_input(self, 'OauthToken', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search term to be applied against tips, category, etc. at a venue.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Radius to search within, in meters. If radius is not specified, a suggested radius will be used depending on the density of venues in the area.)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Section(self, value):
        """
        Set the value of the Section input for this Choreo. ((optional, string) One of food, drinks, coffee, shops, arts, or outdoors. Choosing one of these limits results to venues with categories matching these terms.)
        """
        InputSet._set_input(self, 'Section', value)

class ExploreResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Explore Choreo.
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

    def getRecommendations(self):
        return FoursquareRecommendations(self.getJSONFromString(self._output.get('Response', [])).get("response", []))

class ExploreChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ExploreResultSet(response, path)
