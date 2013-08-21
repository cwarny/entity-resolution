# -*- coding: utf-8 -*-

###############################################################################
#
# ByCoordinates
# Retrieves weather and UV index data for a given Geo point using the Yahoo Weather and EnviroFacts APIs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GetWeather/ByCoordinates')


    def new_input_set(self):
        return ByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return ByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByCoordinatesChoreographyExecution(session, exec_id, path)

class ByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((optional, json) A JSON dictionary containing a Yahoo App ID. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate to use when looking up weather information.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate to use when looking up weather information.)
        """
        InputSet._set_input(self, 'Longitude', value)

class ByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) Contains combined weather data from Yahoo Weather and EnviroFacts.)
        """
        return self._output.get('Response', None)

class ByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByCoordinatesResultSet(response, path)
