# -*- coding: utf-8 -*-

###############################################################################
#
# GetExamples
# Retrieves the examples of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetExamples(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetExamples Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetExamples')


    def new_input_set(self):
        return GetExamplesInputSet()

    def _make_result_set(self, result, path):
        return GetExamplesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetExamplesChoreographyExecution(session, exec_id, path)

class GetExamplesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetExamples
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
    def set_Duplicates(self, value):
        """
        Set the value of the Duplicates input for this Choreo. ((optional, string) Shows duplicate examples from different sources when set to true. Defaults to false.)
        """
        InputSet._set_input(self, 'Duplicates', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Results to skip. Defaults to 0.)
        """
        InputSet._set_input(self, 'Skip', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        InputSet._set_input(self, 'Word', value)

class GetExamplesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetExamples Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetExamplesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetExamplesResultSet(response, path)
