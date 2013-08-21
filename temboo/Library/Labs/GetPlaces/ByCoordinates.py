# -*- coding: utf-8 -*-

###############################################################################
#
# ByCoordinates
# Retrieves information about places near a set of coordinates from multiple sources in one API call.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GetPlaces/ByCoordinates')


    def new_input_set(self):
        return ByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return ByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByCoordinatesChoreographyExecution(session, exec_id, path)

class ByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((required, json) A JSON dictionary of credentials for the APIs you wish to access. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude of the user's location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Limits the number of Foursquare venue results.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude of the user's location.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) This keyword input can be used to narrow search results for Google Places and Foursquare.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Filters results by type of place, such as: bar, dentist, etc. This is used to filter results for Google Places and Yelp.)
        """
        InputSet._set_input(self, 'Type', value)

class ByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (Contains the merged results from the API responses.)
        """
        return self._output.get('Response', None)

class ByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByCoordinatesResultSet(response, path)
