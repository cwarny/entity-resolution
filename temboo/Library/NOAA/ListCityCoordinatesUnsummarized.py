# -*- coding: utf-8 -*-

###############################################################################
#
# ListCityCoordinatesUnsummarized
# Retrieve unsummarized latitude and longitude data for a specified list of cities.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListCityCoordinatesUnsummarized(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListCityCoordinatesUnsummarized Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NOAA/ListCityCoordinatesUnsummarized')


    def new_input_set(self):
        return ListCityCoordinatesUnsummarizedInputSet()

    def _make_result_set(self, result, path):
        return ListCityCoordinatesUnsummarizedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListCityCoordinatesUnsummarizedChoreographyExecution(session, exec_id, path)

class ListCityCoordinatesUnsummarizedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListCityCoordinatesUnsummarized
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CitiesLevel(self, value):
        """
        Set the value of the CitiesLevel input for this Choreo. ((integer) Enter a city grouping number to retrieve its latitude and longitude coordinates. For example: enter 1, to obtain information for primary U.S. cities.)
        """
        InputSet._set_input(self, 'CitiesLevel', value)

class ListCityCoordinatesUnsummarizedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListCityCoordinatesUnsummarized Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((XML) Response from NDFD servers.)
        """
        return self._output.get('Response', None)

class ListCityCoordinatesUnsummarizedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListCityCoordinatesUnsummarizedResultSet(response, path)
