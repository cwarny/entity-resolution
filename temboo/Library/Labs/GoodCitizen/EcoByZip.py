# -*- coding: utf-8 -*-

###############################################################################
#
# EcoByZip
# Returns a host of eco-conscious environmental information for a specified location based on zip code.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class EcoByZip(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the EcoByZip Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Labs/GoodCitizen/EcoByZip')


    def new_input_set(self):
        return EcoByZipInputSet()

    def _make_result_set(self, result, path):
        return EcoByZipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return EcoByZipChoreographyExecution(session, exec_id, path)

class EcoByZipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the EcoByZip
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APICredentials(self, value):
        """
        Set the value of the APICredentials input for this Choreo. ((optional, string) A JSON dictionary containing credentials for Genability. See Choreo documentation for formatting examples.)
        """
        InputSet._set_input(self, 'APICredentials', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of facility records to search for in the Envirofacts database.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Zip(self, value):
        """
        Set the value of the Zip input for this Choreo. ((required, integer) The zip code for the user's current location.)
        """
        InputSet._set_input(self, 'Zip', value)

class EcoByZipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the EcoByZip Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from the Eco Choreo.)
        """
        return self._output.get('Response', None)

class EcoByZipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return EcoByZipResultSet(response, path)
