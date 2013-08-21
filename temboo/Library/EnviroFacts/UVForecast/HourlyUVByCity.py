# -*- coding: utf-8 -*-

###############################################################################
#
# HourlyUVByCity
# Retrieves EPA hourly Ultraviolet (UV) Index readings in a given city. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HourlyUVByCity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HourlyUVByCity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/UVForecast/HourlyUVByCity')


    def new_input_set(self):
        return HourlyUVByCityInputSet()

    def _make_result_set(self, result, path):
        return HourlyUVByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HourlyUVByCityChoreographyExecution(session, exec_id, path)

class HourlyUVByCityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HourlyUVByCity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) A valid City Name in the United States.)
        """
        InputSet._set_input(self, 'City', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Results can be retrieved in either JSON or XML. Defaults to XML.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) The abbreviation of the state that the city resides in.)
        """
        InputSet._set_input(self, 'State', value)

class HourlyUVByCityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HourlyUVByCity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class HourlyUVByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HourlyUVByCityResultSet(response, path)
