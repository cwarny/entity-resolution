# -*- coding: utf-8 -*-

###############################################################################
#
# Pet
# Returns lifecycle food production and veterinary care emissions modeling for domestic animals.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Pet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Pet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/BrighterPlanet/Pet')


    def new_input_set(self):
        return PetInputSet()

    def _make_result_set(self, result, path):
        return PetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PetChoreographyExecution(session, exec_id, path)

class PetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Pet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Brighter Planet.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Acquisition(self, value):
        """
        Set the value of the Acquisition input for this Choreo. ((optional, string) Enter date the pet was acquired.)
        """
        InputSet._set_input(self, 'Acquisition', value)
    def set_Breed(self, value):
        """
        Set the value of the Breed input for this Choreo. ((optional, string) Enter a cat, dog, or horse breed.)
        """
        InputSet._set_input(self, 'Breed', value)
    def set_Gender(self, value):
        """
        Set the value of the Gender input for this Choreo. ((optional, string) Enter cat, dog, or horse gender.)
        """
        InputSet._set_input(self, 'Gender', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Specify your desired response format. Accepted values are xml and json (the default).)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Retirement(self, value):
        """
        Set the value of the Retirement input for this Choreo. ((optional, string) Enter date you no longer have the pet.)
        """
        InputSet._set_input(self, 'Retirement', value)
    def set_Species(self, value):
        """
        Set the value of the Species input for this Choreo. ((optional, string) Enter the species type (e.g. bird, cat, dog, ferret, fish).)
        """
        InputSet._set_input(self, 'Species', value)
    def set_Weight(self, value):
        """
        Set the value of the Weight input for this Choreo. ((optional, decimal) Enter pet weight in kilograms.)
        """
        InputSet._set_input(self, 'Weight', value)

class PetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Pet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Brighter Planet.)
        """
        return self._output.get('Response', None)

class PetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PetResultSet(response, path)
