# -*- coding: utf-8 -*-

###############################################################################
#
# HourlyUVByZipCode
# Retrieves EPA hourly Ultraviolet (UV) Index readings in a given zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HourlyUVByZipCode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HourlyUVByZipCode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/EnviroFacts/UVForecast/HourlyUVByZipCode')


    def new_input_set(self):
        return HourlyUVByZipCodeInputSet()

    def _make_result_set(self, result, path):
        return HourlyUVByZipCodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HourlyUVByZipCodeChoreographyExecution(session, exec_id, path)

class HourlyUVByZipCodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HourlyUVByZipCode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Results can be retrieved in either JSON or XML. Defaults to XML.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, integer) A valid United States Postal Service (USPS) ZIP Code or Postal Code.)
        """
        InputSet._set_input(self, 'Zip', value)

class HourlyUVByZipCodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HourlyUVByZipCode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from EnviroFacts.)
        """
        return self._output.get('Response', None)

class HourlyUVByZipCodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HourlyUVByZipCodeResultSet(response, path)
