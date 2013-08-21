# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByID
# Retrieves local NPR member stations based on their unique ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NPR/StationFinder/SearchByID')


    def new_input_set(self):
        return SearchByIDInputSet()

    def _make_result_set(self, result, path):
        return SearchByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByIDChoreographyExecution(session, exec_id, path)

class SearchByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NPR.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The unique ID that NPR asociates with the organization.)
        """
        InputSet._set_input(self, 'ID', value)

class SearchByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) )
        """
        return self._output.get('Response', None)

class SearchByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByIDResultSet(response, path)
