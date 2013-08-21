# -*- coding: utf-8 -*-

###############################################################################
#
# FindRestaurantsByName
# Search for restaurants by name. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FindRestaurantsByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FindRestaurantsByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Factual/FindRestaurantsByName')


    def new_input_set(self):
        return FindRestaurantsByNameInputSet()

    def _make_result_set(self, result, path):
        return FindRestaurantsByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FindRestaurantsByNameChoreographyExecution(session, exec_id, path)

class FindRestaurantsByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FindRestaurantsByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Factual (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Factual (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A search string (i.e. Starbucks))
        """
        InputSet._set_input(self, 'Query', value)

class FindRestaurantsByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FindRestaurantsByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Factual.)
        """
        return self._output.get('Response', None)

class FindRestaurantsByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FindRestaurantsByNameResultSet(response, path)
