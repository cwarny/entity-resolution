# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByName
# Searches for politicians, individuals, or organizations with the given name. Returns basic information about the the contributions to and from the entity that is specified.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/SearchByName')


    def new_input_set(self):
        return SearchByNameInputSet()

    def _make_result_set(self, result, path):
        return SearchByNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByNameChoreographyExecution(session, exec_id, path)

class SearchByNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API key provided by Sunlight Data Services.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Search(self, value):
        """
        Set the value of the Search input for this Choreo. ((required, string) The query string.)
        """
        InputSet._set_input(self, 'Search', value)

class SearchByNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Influence Explorer.)
        """
        return self._output.get('Response', None)

class SearchByNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByNameResultSet(response, path)
