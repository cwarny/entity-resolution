# -*- coding: utf-8 -*-

###############################################################################
#
# ByKloutID
# Performs a lookup for a user's identity using a Klout ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ByKloutID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ByKloutID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Klout/Identity/ByKloutID')


    def new_input_set(self):
        return ByKloutIDInputSet()

    def _make_result_set(self, result, path):
        return ByKloutIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ByKloutIDChoreographyExecution(session, exec_id, path)

class ByKloutIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ByKloutID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Klout.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_KloutID(self, value):
        """
        Set the value of the KloutID input for this Choreo. ((required, integer) The numeric ID for a Klout user.)
        """
        InputSet._set_input(self, 'KloutID', value)

class ByKloutIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ByKloutID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Klout.)
        """
        return self._output.get('Response', None)

class ByKloutIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ByKloutIDResultSet(response, path)
