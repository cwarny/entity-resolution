# -*- coding: utf-8 -*-

###############################################################################
#
# EcoByCoordinates
# Returns a host of eco-conscious environmental information for a specified location based on Lattitude and Longitude inputs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EcoByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EcoByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GoodCitizen/EcoByCoordinates')


    def new_input_set(self):
        return EcoByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return EcoByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EcoByCoordinatesChoreographyExecution(session, exec_id, path)

class EcoByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EcoByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((optional, string) A JSON dictionary containing credentials for Genability. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude coordinate for the user's current location.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of facility records to search for in the Envirofacts database.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude coordinate for the user's current location.)
        """
        InputSet._set_input(self, 'Longitude', value)

class EcoByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EcoByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from the Eco Choreo.)
        """
        return self._output.get('Response', None)

class EcoByCoordinatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EcoByCoordinatesResultSet(response, path)
