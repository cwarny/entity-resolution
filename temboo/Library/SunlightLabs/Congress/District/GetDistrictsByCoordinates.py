# -*- coding: utf-8 -*-

###############################################################################
#
# GetDistrictsByCoordinates
# Returns the district that a set of latitude/longitude coordinates falls within.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetDistrictsByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetDistrictsByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/District/GetDistrictsByCoordinates')


    def new_input_set(self):
        return GetDistrictsByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetDistrictsByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetDistrictsByCoordinatesChoreographyExecution(session, exec_id, path)

class GetDistrictsByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetDistrictsByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate of the area that a legislator represents.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate of the area that a legislator represents.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetDistrictsByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetDistrictsByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class GetDistrictsByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetDistrictsByCoordinatesResultSet(response, path)
