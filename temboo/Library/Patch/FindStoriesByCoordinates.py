# -*- coding: utf-8 -*-

###############################################################################
#
# FindStoriesByCoordinates
# Return the most recent stories from a specified U.S. latitude and longitude.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindStoriesByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindStoriesByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Patch/FindStoriesByCoordinates')


    def new_input_set(self):
        return FindStoriesByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return FindStoriesByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindStoriesByCoordinatesChoreographyExecution(session, exec_id, path)

class FindStoriesByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindStoriesByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) A valid API key provided by Patch.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((required, string) The API shared secret provided by Patch.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Keyword(self, value):
        """
        Set the value of the Keyword input for this Choreo. ((optional, string) Specify one or more words or phrases to find in the story title, story summary, and topic tags of the stories to return.)
        """
        InputSet._set_input(self, 'Keyword', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitiude for the area from which to retrieve stories. For example, "40.740512".)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Specify how many stories to return, between 1 and 100. The default is 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude for the area from which to retrieve stories. For example, "-73.991479".)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_MaximumAge(self, value):
        """
        Set the value of the MaximumAge input for this Choreo. ((optional, integer) Specify the maximum age in days of the stories to return, between 1 and 30. The default is 10.)
        """
        InputSet._set_input(self, 'MaximumAge', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) Specify a radius in feet in which to search the specified coordinates, between 500 and 26,400. The default is 1,000 feet.)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify "xml" to convert the Patch JSON response to XML. The default is "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class FindStoriesByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindStoriesByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response returned from Patch.)
        """
        return self._output.get('Response', None)

class FindStoriesByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindStoriesByCoordinatesResultSet(response, path)
