# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByLocation
# Retrieves local NPR member stations near the specified lattitude and longitude location coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByLocation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByLocation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByLocation')


    def new_input_set(self):
        return SearchByLocationInputSet()

    def _make_result_set(self, result, path):
        return SearchByLocationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByLocationChoreographyExecution(session, exec_id, path)

class SearchByLocationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByLocation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Lattitude(self, value):
        """
        Set the value of the Lattitude input for this Choreo. ((required, decimal) The lattitude point of a station's location. Must be used together with the longitude parameter. This must be a positive value.)
        """
        InputSet._set_input(self, 'Lattitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude point of a station's location. Must be used together with the lattitude parameter. This must be a positive value.)
        """
        InputSet._set_input(self, 'Longitude', value)

class SearchByLocationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByLocation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class SearchByLocationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByLocationResultSet(response, path)
