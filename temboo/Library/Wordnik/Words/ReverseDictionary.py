# -*- coding: utf-8 -*-

###############################################################################
#
# ReverseDictionary
# Retrieves a reverse dictionary search for a given word.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReverseDictionary(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReverseDictionary Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Words/ReverseDictionary')


    def new_input_set(self):
        return ReverseDictionaryInputSet()

    def _make_result_set(self, result, path):
        return ReverseDictionaryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReverseDictionaryChoreographyExecution(session, exec_id, path)

class ReverseDictionaryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReverseDictionary
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
    def set_ExcludeSource(self, value):
        """
        Set the value of the ExcludeSource input for this Choreo. ((optional, string) Exclude these comma-delimited source dictionaries: ahd, century, wiktionary,webster, wordnet.)
        """
        InputSet._set_input(self, 'ExcludeSource', value)
    def set_ExpandTerms(self, value):
        """
        Set the value of the ExpandTerms input for this Choreo. ((optional, any) Expand terms by either: synonym or hypernym.)
        """
        InputSet._set_input(self, 'ExpandTerms', value)
    def set_IncludePartOfSpeech(self, value):
        """
        Set the value of the IncludePartOfSpeech input for this Choreo. ((optional, string) Only includes the specified comma-delimited parts of speech. Acceptable values include: adjective, noun, etc. See docs for full list.)
        """
        InputSet._set_input(self, 'IncludePartOfSpeech', value)
    def set_IncludeSource(self, value):
        """
        Set the value of the IncludeSource input for this Choreo. ((optional, string) Only include these comma-delimited source dictionaries: ahd, century, wiktionary,webster, wordnet.)
        """
        InputSet._set_input(self, 'IncludeSource', value)
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
    def set_MinLength(self, value):
        """
        Set the value of the MinLength input for this Choreo. ((optional, integer) ‪Minimum word length.)
        """
        InputSet._set_input(self, 'MinLength', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Word or fragment to query for in Wordnik.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)
    def set_Skip(self, value):
        """
        Set the value of the Skip input for this Choreo. ((optional, integer) Number of results to skip.)
        """
        InputSet._set_input(self, 'Skip', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Results can be sorted by: alpha, count, or length.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Indicate the order to sort, either asc (ascending) or desc (descending).)
        """
        InputSet._set_input(self, 'SortOrder', value)
    def set_WordSense(self, value):
        """
        Set the value of the WordSense input for this Choreo. ((optional, string) Restricts words and finds the closest sense to the one indicated.)
        """
        InputSet._set_input(self, 'WordSense', value)

class ReverseDictionaryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReverseDictionary Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class ReverseDictionaryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReverseDictionaryResultSet(response, path)
