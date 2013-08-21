# -*- coding: utf-8 -*-

###############################################################################
#
# DeletePlace
# Delete a new Place from Google Places.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeletePlace(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeletePlace Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Places/DeletePlace')


    def new_input_set(self):
        return DeletePlaceInputSet()

    def _make_result_set(self, result, path):
        return DeletePlaceResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePlaceChoreographyExecution(session, exec_id, path)

class DeletePlaceInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeletePlace
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((required, string) Enter your Google API key.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_PlaceReference(self, value):
        """
        Set the value of the PlaceReference input for this Choreo. ((required, string) The unique place reference. This is returned in the PlaceSearch Choreo.)
        """
        InputSet._set_input(self, 'PlaceReference', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sensor(self, value):
        """
        Set the value of the Sensor input for this Choreo. ((optional, boolean) Indicates whether or not the directions request is from a device with a location sensor. Value must be either 1 or 0. Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'Sensor', value)

class DeletePlaceResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeletePlace Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google.)
        """
        return self._output.get('Response', None)

class DeletePlaceChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePlaceResultSet(response, path)
