# -*- coding: utf-8 -*-

###############################################################################
#
# GetDemographicsByCoordinates
# Retrieve demographic information for specified geographical coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDemographicsByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDemographicsByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/DataGov/GetDemographicsByCoordinates')


    def new_input_set(self):
        return GetDemographicsByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetDemographicsByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDemographicsByCoordinatesChoreographyExecution(session, exec_id, path)

class GetDemographicsByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDemographicsByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_DataVersion(self, value):
        """
        Set the value of the DataVersion input for this Choreo. ((optional, string) Specify the data version to search, such as "jun2011" (the default).)
        """
        InputSet._set_input(self, 'DataVersion', value)
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

class GetDemographicsByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDemographicsByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from the API.)
        """
        return self._output.get('Response', None)

class GetDemographicsByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDemographicsByCoordinatesResultSet(response, path)
