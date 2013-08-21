# -*- coding: utf-8 -*-

###############################################################################
#
# FindByCoordinates
# Returns a place ID for a given latitude, longitude and accuracy.
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
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Places/FindByCoordinates')


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
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Accuracy(self, value):
        """
        Set the value of the Accuracy input for this Choreo. ((optional, integer) Recorded accuracy level of the location information. Valid range is 1-16. The default is 16.)
        """
        InputSet._set_input(self, 'Accuracy', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude whose valid range is -90 to 90. Anything more than 4 decimal places will be truncated.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude whose valid range is -180 to 180. Anything more than 4 decimal places will be truncated.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) )
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
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class FindByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindByCoordinatesResultSet(response, path)
