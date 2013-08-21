# -*- coding: utf-8 -*-

###############################################################################
#
# WeatherByCitiesSummarized
# Retrieve weather information for a specific list of cities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class WeatherByCitiesSummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the WeatherByCitiesSummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NOAA/WeatherByCitiesSummarized')


    def new_input_set(self):
        return WeatherByCitiesSummarizedInputSet()

    def _make_result_set(self, result, path):
        return WeatherByCitiesSummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return WeatherByCitiesSummarizedChoreographyExecution(session, exec_id, path)

class WeatherByCitiesSummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the WeatherByCitiesSummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CitiesLevel(self, value):
        """
        Set the value of the CitiesLevel input for this Choreo. ((required, integer) Enter a city grouping number. For example: enter 1, to obtain weather information for primary U.S. cities. See documentation for additional numbers.)
        """
        InputSet._set_input(self, 'CitiesLevel', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((required, string) Specify a timespan for which NDFD data will be summarized. Enter: 24 hourly, for a 24 hour summary, or: 12 hourly, for a 12 hour weather summary.)
        """
        InputSet._set_input(self, 'Format', value)
    def set_NumberOfDays(self, value):
        """
        Set the value of the NumberOfDays input for this Choreo. ((optional, integer) Specify the number of days to retieve data for. If null, data from the earliest date in the dabase is returned.)
        """
        InputSet._set_input(self, 'NumberOfDays', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, date) Enter the start time for retrieval of NDWD information in UTC format. If null, the earliest date in the database is returned. Format: 2004-04-27T12:00.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_Unit(self, value):
        """
        Set the value of the Unit input for this Choreo. ((optional, string) Enter the unit format the data will be displayed in. Default is: e, for Standard English (U.S. Standard).  Or: m, for Metric (SI Units).)
        """
        InputSet._set_input(self, 'Unit', value)

class WeatherByCitiesSummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the WeatherByCitiesSummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class WeatherByCitiesSummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return WeatherByCitiesSummarizedResultSet(response, path)
