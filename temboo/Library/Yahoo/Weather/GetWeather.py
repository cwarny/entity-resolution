# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeather
# Retrieves the Yahoo! Weather RSS Feed for any specified location.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWeather(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWeather Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Weather/GetWeather')


    def new_input_set(self):
        return GetWeatherInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherChoreographyExecution(session, exec_id, path)

class GetWeatherInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWeather
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celsius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        InputSet._set_input(self, 'Units', value)
    def set_WOEID(self, value):
        """
        Set the value of the WOEID input for this Choreo. ((required, integer) Where On Earth ID for the desired location. This unique integer can be found by first running the GetWeatherByCoordinates Choreo.)
        """
        InputSet._set_input(self, 'WOEID', value)

class GetWeatherResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWeather Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Yahoo! Weather.)
        """
        return self._output.get('Response', None)

class GetWeatherChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeatherResultSet(response, path)
