# -*- coding: utf-8 -*-

###############################################################################
#
# ByTwitterScreenName
# Performs a lookup for a user's identity using a Twitter screen name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByTwitterScreenName(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByTwitterScreenName Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByTwitterScreenName')


    def new_input_set(self):
        return ByTwitterScreenNameInputSet()

    def _make_result_set(self, result, path):
        return ByTwitterScreenNameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByTwitterScreenNameChoreographyExecution(session, exec_id, path)

class ByTwitterScreenNameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByTwitterScreenName
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Klout.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((required, string) The screen name for a Twitter user.)
        """
        InputSet._set_input(self, 'ScreenName', value)

class ByTwitterScreenNameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByTwitterScreenName Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Klout.)
        """
        return self._output.get('Response', None)

class ByTwitterScreenNameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByTwitterScreenNameResultSet(response, path)
