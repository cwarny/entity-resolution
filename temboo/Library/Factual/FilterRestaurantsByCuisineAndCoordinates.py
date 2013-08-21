# -*- coding: utf-8 -*-

###############################################################################
#
# FilterRestaurantsByCuisineAndCoordinates
# Find restaurants by cuisine and near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FilterRestaurantsByCuisineAndCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FilterRestaurantsByCuisineAndCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Factual/FilterRestaurantsByCuisineAndCoordinates')


    def new_input_set(self):
        return FilterRestaurantsByCuisineAndCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FilterRestaurantsByCuisineAndCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FilterRestaurantsByCuisineAndCoordinatesChoreographyExecution(session, exec_id, path)

class FilterRestaurantsByCuisineAndCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FilterRestaurantsByCuisineAndCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Cuisine(self, value):
        """
        Set the value of the Cuisine input for this Choreo. ((required, string) Enter a desired cuisine to narrow the search results. See Choreo doc for a list of available cuisine parameters.)
        """
        InputSet._set_input(self, 'Cuisine', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Enter latitude coordinates of the location defining the center of the search radius.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter longitude coordinates of the location defining the center of the search radius.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        InputSet._set_input(self, 'Radius', value)

class FilterRestaurantsByCuisineAndCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FilterRestaurantsByCuisineAndCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FilterRestaurantsByCuisineAndCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FilterRestaurantsByCuisineAndCoordinatesResultSet(response, path)
