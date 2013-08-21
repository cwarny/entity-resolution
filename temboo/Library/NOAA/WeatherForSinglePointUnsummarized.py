# -*- coding: utf-8 -*-

###############################################################################
#
# WeatherForSinglePointUnsummarized
# Retrieve unsummarized weather information for a single point defined by latitude and longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WeatherForSinglePointUnsummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WeatherForSinglePointUnsummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherForSinglePointUnsummarized')


    def new_input_set(self):
        return WeatherForSinglePointUnsummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherForSinglePointUnsummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherForSinglePointUnsummarizedChoreographyExecution(session, exec_id, path)

class WeatherForSinglePointUnsummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WeatherForSinglePointUnsummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Enter the end time for retrieval of NDWD information in UTC format. If null, the last available time in the database is returned. Format: 2004-04-27T12:00.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Enter the latitude coordinate of the point for which weather data is requested. North latitude is positive.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Enter the longitude coordinate of the point for which weather data is requested. West longitude is negative.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Product(self, value):
        """
        Set the value of the Product input for this Choreo. ((required, string) Enter one of two parameters: time-series (to return all data between the Begin and End time parameters); glance for a subset of 5 often used parameters)
        """
        InputSet._set_input(self, 'Product', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest time in the database is returned. Format: 2004-04-27T12:00.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        InputSet._set_input(self, 'Unit', value)

class WeatherForSinglePointUnsummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WeatherForSinglePointUnsummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class WeatherForSinglePointUnsummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherForSinglePointUnsummarizedResultSet(response, path)
