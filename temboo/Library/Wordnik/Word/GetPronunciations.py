# -*- coding: utf-8 -*-

###############################################################################
#
# GetPronunciations
# Retrieves the pronuciation of a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPronunciations(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPronunciations Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Word/GetPronunciations')


    def new_input_set(self):
        return GetPronunciationsInputSet()

    def _make_result_set(self, result, path):
        return GetPronunciationsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPronunciationsChoreographyExecution(session, exec_id, path)

class GetPronunciationsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPronunciations
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
    def set_Dictionary(self, value):
        """
        Set the value of the Dictionary input for this Choreo. ((optional, string) Source dictionary to return pronunciation from. Acceptable values: ahd, century, cmu, macmillan, wiktionary,webster, wordnet.)
        """
        InputSet._set_input(self, 'Dictionary', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 50.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_TypeFormat(self, value):
        """
        Set the value of the TypeFormat input for this Choreo. ((optional, string) Text pronunciation type. Acceptable values: ahd, arpabet, gcide-diacritical, IPA.)
        """
        InputSet._set_input(self, 'TypeFormat', value)
    def set_Word(self, value):
        """
        Set the value of the Word input for this Choreo. ((required, string) The word you want to look up on Wordnik.)
        """
        InputSet._set_input(self, 'Word', value)

class GetPronunciationsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPronunciations Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetPronunciationsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPronunciationsResultSet(response, path)
