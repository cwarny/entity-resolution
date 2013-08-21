# -*- coding: utf-8 -*-

###############################################################################
#
# GetWeatherByAddress
# Retrieves the Yahoo Weather RSS Feed for any specified location by address.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetWeatherByAddress(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetWeatherByAddress Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/Weather/GetWeatherByAddress')


    def new_input_set(self):
        return GetWeatherByAddressInputSet()

    def _make_result_set(self, result, path):
        return GetWeatherByAddressResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetWeatherByAddressChoreographyExecution(session, exec_id, path)

class GetWeatherByAddressInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetWeatherByAddress
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Address(self, value):
        """
        Set the value of the Address input for this Choreo. ((required, string) The address to be searched.)
        """
        InputSet._set_input(self, 'Address', value)
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) The App ID provided by Yahoo!)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) The unit of temperature in the response. Acceptable inputs: f for Fahrenheit or c for Celsius. Defaults to f. When c is specified, all units measurements returned are changed to metric.)
        """
        InputSet._set_input(self, 'Units', value)

class GetWeatherByAddressResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetWeatherByAddress Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Yahoo Weather.)
        """
        return self._output.get('Response', None)
    def get_WOEID(self):
        """
        Retrieve the value for the "WOEID" output from this Choreo execution. ((integer) The unique Where On Earth ID of the location.)
        """
        return self._output.get('WOEID', None)

class GetWeatherByAddressChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetWeatherByAddressResultSet(response, path)
