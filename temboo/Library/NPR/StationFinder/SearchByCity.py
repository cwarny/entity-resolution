# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByCity
# Retrieves local NPR member stations based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByCity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByCity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByCity')


    def new_input_set(self):
        return SearchByCityInputSet()

    def _make_result_set(self, result, path):
        return SearchByCityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCityChoreographyExecution(session, exec_id, path)

class SearchByCityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByCity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_City(self, value):
        """
        Set the value of the City input for this Choreo. ((required, string) Enter the city name. When searching by city, the state parameter must also be specified.)
        """
        InputSet._set_input(self, 'City', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((required, string) Enter the state. The city parameter must also be specified.)
        """
        InputSet._set_input(self, 'State', value)

class SearchByCityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByCity Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class SearchByCityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCityResultSet(response, path)
