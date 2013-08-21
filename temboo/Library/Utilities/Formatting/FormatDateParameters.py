# -*- coding: utf-8 -*-

###############################################################################
#
# FormatDateParameters
# Returns the specified date parameters as the number of milliseconds since January 1, 1970 (epoch time).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FormatDateParameters(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FormatDateParameters Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Formatting/FormatDateParameters')


    def new_input_set(self):
        return FormatDateParametersInputSet()

    def _make_result_set(self, result, path):
        return FormatDateParametersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FormatDateParametersChoreographyExecution(session, exec_id, path)

class FormatDateParametersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FormatDateParameters
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Day(self, value):
        """
        Set the value of the Day input for this Choreo. ((required, integer) Sets the day (1–31) of the timestamp.)
        """
        InputSet._set_input(self, 'Day', value)
    def set_Hour(self, value):
        """
        Set the value of the Hour input for this Choreo. ((optional, integer) Sets the hours (0–23) of the timestamp.)
        """
        InputSet._set_input(self, 'Hour', value)
    def set_Minute(self, value):
        """
        Set the value of the Minute input for this Choreo. ((optional, integer) Sets the minutes (0–59) of the timestamp.)
        """
        InputSet._set_input(self, 'Minute', value)
    def set_Month(self, value):
        """
        Set the value of the Month input for this Choreo. ((required, integer) Sets the month (1–12) of the timestamp.)
        """
        InputSet._set_input(self, 'Month', value)
    def set_Second(self, value):
        """
        Set the value of the Second input for this Choreo. ((optional, integer) Sets the seconds (0–59) of the timestamp.)
        """
        InputSet._set_input(self, 'Second', value)
    def set_Year(self, value):
        """
        Set the value of the Year input for this Choreo. ((required, integer) Sets the year of the timestamp.)
        """
        InputSet._set_input(self, 'Year', value)

class FormatDateParametersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FormatDateParameters Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Timestamp(self):
        """
        Retrieve the value for the "Timestamp" output from this Choreo execution. ((date) A number representing the specified date and time, expressed as the number of milliseconds since January 1, 1970 (epoch time). )
        """
        return self._output.get('Timestamp', None)

class FormatDateParametersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FormatDateParametersResultSet(response, path)
