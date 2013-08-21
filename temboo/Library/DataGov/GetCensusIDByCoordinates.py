# -*- coding: utf-8 -*-

###############################################################################
#
# GetCensusIDByCoordinates
# Retrieve the U.S. census block geography ID for a specified latitude and longitude. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetCensusIDByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetCensusIDByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetCensusIDByCoordinates')


    def new_input_set(self):
        return GetCensusIDByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetCensusIDByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetCensusIDByCoordinatesChoreographyExecution(session, exec_id, path)

class GetCensusIDByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetCensusIDByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_GeographyType(self, value):
        """
        Set the value of the GeographyType input for this Choreo. ((required, string) Specify one of the following geography type values: "state", "county", "tract", "block", "congdistrict", "statehouse", "statesenate", "censusplace", or "msa" (metropolitan statistical area).)
        """
        InputSet._set_input(self, 'GeographyType', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) Specify a latitude to search for, such as "41.486857".)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) Specify a longitude to search for, such as "-71.294392".)
        """
        InputSet._set_input(self, 'Longitude', value)

class GetCensusIDByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetCensusIDByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CensusID(self):
        """
        Retrieve the value for the "CensusID" output from this Choreo execution. ((integer) The ID retrieved from the API call.)
        """
        return self._output.get('CensusID', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetCensusIDByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetCensusIDByCoordinatesResultSet(response, path)
