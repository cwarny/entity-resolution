# -*- coding: utf-8 -*-

###############################################################################
#
# WeatherByZipcode
# Retrieve DWML-encoded NDFD data for a specified zipcode (in 50 U.S. States and Puerto Rico).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WeatherByZipcode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WeatherByZipcode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherByZipcode')


    def new_input_set(self):
        return WeatherByZipcodeInputSet()

    def _make_result_set(self, result, path):
        return WeatherByZipcodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherByZipcodeChoreographyExecution(session, exec_id, path)

class WeatherByZipcodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WeatherByZipcode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Enter today's date, or some future date in UTC format. Format: 2004-04-27T12:00. Defaults to NOW if not provided.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_NDFDParameterName(self, value):
        """
        Set the value of the NDFDParameterName input for this Choreo. ((optional, string) Enter an additional weather parameter in the following format: phail=phail. Use only if Product is set to: glance.)
        """
        InputSet._set_input(self, 'NDFDParameterName', value)
    def set_Product(self, value):
        """
        Set the value of the Product input for this Choreo. ((required, string) Enter one of two parameters: time-series (to return all data between the Begin and End time parameters); glance for a subset of 5 often used parameters)
        """
        InputSet._set_input(self, 'Product', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest date in the database is returned.  Format: 2004-04-27T12:00.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        InputSet._set_input(self, 'Unit', value)
    def set_ZipCodeList(self, value):
        """
        Set the value of the ZipCodeList input for this Choreo. ((required, integer) Enter the zipcode for which NDFD weather information will be retrieved.)
        """
        InputSet._set_input(self, 'ZipCodeList', value)

class WeatherByZipcodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WeatherByZipcode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class WeatherByZipcodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherByZipcodeResultSet(response, path)
