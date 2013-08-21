# -*- coding: utf-8 -*-

###############################################################################
#
# RandomWord
# Retrieves a random word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RandomWord(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RandomWord Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/RandomWord')


    def new_input_set(self):
        return RandomWordInputSet()

    def _make_result_set(self, result, path):
        return RandomWordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RandomWordChoreographyExecution(session, exec_id, path)

class RandomWordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RandomWord
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ExcludePartOfSpeech(self, value):
        """
        Set the value of the ExcludePartOfSpeech input for this Choreo. ((optional, string) Excludes the specified comma-delimited parts of speech from the results returned. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        InputSet._set_input(self, 'ExcludePartOfSpeech', value)
    def set_HasDefinition(self, value):
        """
        Set the value of the HasDefinition input for this Choreo. ((optional, string) Only returns words that have dictionary definitions when true. Otherwise false. Defaults to true.)
        """
        InputSet._set_input(self, 'HasDefinition', value)
    def set_IncludePartOfSpeech(self, value):
        """
        Set the value of the IncludePartOfSpeech input for this Choreo. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        InputSet._set_input(self, 'IncludePartOfSpeech', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) Maximum number of results to return. Defaults to 10.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_MaxCorpus(self, value):
        """
        Set the value of the MaxCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count below the given number.)
        """
        InputSet._set_input(self, 'MaxCorpus', value)
    def set_MaxDictionaries(self, value):
        """
        Set the value of the MaxDictionaries input for this Choreo. ((optional, integer) Maximum number of dictionaries in which the words appear.)
        """
        InputSet._set_input(self, 'MaxDictionaries', value)
    def set_MaxLength(self, value):
        """
        Set the value of the MaxLength input for this Choreo. ((optional, integer) Maximum word length.)
        """
        InputSet._set_input(self, 'MaxLength', value)
    def set_MinCorpus(self, value):
        """
        Set the value of the MinCorpus input for this Choreo. ((optional, integer) Results include a corpus frequency count for each word returned. When this input is specified, results are limited to words with a corpus frequency count above the given number.)
        """
        InputSet._set_input(self, 'MinCorpus', value)
    def set_MinDictionaries(self, value):
        """
        Set the value of the MinDictionaries input for this Choreo. ((optional, integer) Minimum number of dictionaries in which the words appear.)
        """
        InputSet._set_input(self, 'MinDictionaries', value)
    def set_MinLength(self, value):
        """
        Set the value of the MinLength input for this Choreo. ((optional, integer) ‪Minimum word length.)
        """
        InputSet._set_input(self, 'MinLength', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)

class RandomWordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RandomWord Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class RandomWordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RandomWordResultSet(response, path)
