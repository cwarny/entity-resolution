# -*- coding: utf-8 -*-

###############################################################################
#
# ByTwitterID
# Performs a lookup for a user's identity using a Twitter ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByTwitterID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByTwitterID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByTwitterID')


    def new_input_set(self):
        return ByTwitterIDInputSet()

    def _make_result_set(self, result, path):
        return ByTwitterIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByTwitterIDChoreographyExecution(session, exec_id, path)

class ByTwitterIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByTwitterID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Klout.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_TwitterID(self, value):
        """
        Set the value of the TwitterID input for this Choreo. ((required, integer) The numeric ID for a Twitter user.)
        """
        InputSet._set_input(self, 'TwitterID', value)

class ByTwitterIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByTwitterID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Klout.)
        """
        return self._output.get('Response', None)

class ByTwitterIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByTwitterIDResultSet(response, path)
