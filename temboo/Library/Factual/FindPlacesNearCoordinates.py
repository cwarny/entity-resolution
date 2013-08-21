# -*- coding: utf-8 -*-

###############################################################################
#
# FindPlacesNearCoordinates
# Find places near specified latitude, longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindPlacesNearCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindPlacesNearCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Factual/FindPlacesNearCoordinates')


    def new_input_set(self):
        return FindPlacesNearCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindPlacesNearCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindPlacesNearCoordinatesChoreographyExecution(session, exec_id, path)

class FindPlacesNearCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindPlacesNearCoordinates
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
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) A search string (i.e. Starbucks))
        """
        InputSet._set_input(self, 'Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((required, integer) Provide the radius (in meters, and centered on the latitude-longitude coordinates specified) for which search results will be returned.)
        """
        InputSet._set_input(self, 'Radius', value)

class FindPlacesNearCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindPlacesNearCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FindPlacesNearCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindPlacesNearCoordinatesResultSet(response, path)
