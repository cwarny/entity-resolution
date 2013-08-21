# -*- coding: utf-8 -*-

###############################################################################
#
# GetEtymology
# Retrieves the etymology of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetEtymology(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetEtymology Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetEtymology')


    def new_input_set(self):
        return GetEtymologyInputSet()

    def _make_result_set(self, result, path):
        return GetEtymologyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetEtymologyChoreographyExecution(session, exec_id, path)

class GetEtymologyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetEtymology
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Cannonical(self, value):
        """
        Set the value of the Cannonical input for this Choreo. ((optional, string) If true will try to return the correct word root ('cats' -> 'cat'). If false returns exactly what was requested. Defaults to false.)
        """
        InputSet._set_input(self, 'Cannonical', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        InputSet._set_input(self, 'Word', value)

class GetEtymologyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetEtymology Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetEtymologyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetEtymologyResultSet(response, path)
