# -*- coding: utf-8 -*-

###############################################################################
#
# FindByCoordinates
# Retrieves complete location information from a specified pair of latitude and longitude coordinates.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Yahoo/PlaceFinder/FindByCoordinates')


    def new_input_set(self):
        return FindByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindByCoordinatesChoreographyExecution(session, exec_id, path)

class FindByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((optional, string) The App ID provided by Yahoo!)
        """
        InputSet._set_input(self, 'AppID', value)
    def set_GeocodeFlags(self, value):
        """
        Set the value of the GeocodeFlags input for this Choreo. ((optional, string) Affects how geocoding is performed for the request. Valid value are: A, C, L, Q, or R. See documentation for more details on this parameter.)
        """
        InputSet._set_input(self, 'GeocodeFlags', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, string) The latitude coordinate of the location you want to find.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, string) The longitude coordinate of the location you want to find.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_ResponseFlags(self, value):
        """
        Set the value of the ResponseFlags input for this Choreo. ((optional, string) Determines which data elements are returned in the response. Valid values are: B, C, D, E, G, I, J, Q, R, T, U, W, X. See documentation for details on this parameter.)
        """
        InputSet._set_input(self, 'ResponseFlags', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) You can specify json to get this output format in JSON. Otherwise, the default output will be in XML.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FindByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Yahoo! PlaceFinder.)
        """
        return self._output.get('Response', None)

class FindByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByCoordinatesResultSet(response, path)
