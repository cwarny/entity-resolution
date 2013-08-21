# -*- coding: utf-8 -*-

###############################################################################
#
# TopPhraseSources
# Returns the top sources of a given phrase, which can be sorted either by legislator, state, party, bioguide ID, volume, or chambers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TopPhraseSources(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TopPhraseSources Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/CapitolWords/TopPhraseSources')


    def new_input_set(self):
        return TopPhraseSourcesInputSet()

    def _make_result_set(self, result, path):
        return TopPhraseSourcesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TopPhraseSourcesChoreographyExecution(session, exec_id, path)

class TopPhraseSourcesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TopPhraseSources
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Chamber(self, value):
        """
        Set the value of the Chamber input for this Choreo. ((optional, string) Limit results to a particular chamber. Valid values: house, senate, extensions.)
        """
        InputSet._set_input(self, 'Chamber', value)
    def set_Date(self, value):
        """
        Set the value of the Date input for this Choreo. ((optional, string) Show results for only the given date. Format: YYYY-MM-DD)
        """
        InputSet._set_input(self, 'Date', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, string) Limit results to those on or before the given date. Format: YYYY-MM-DD.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Entity(self, value):
        """
        Set the value of the Entity input for this Choreo. ((required, string) The type of entity for which to return top results. Acceptable inputs: legislator, state, party, bioguide_id, volume, chamber. So 'legislator' returns the top legislators who say the given phrase.)
        """
        InputSet._set_input(self, 'Entity', value)
    def set_MinCount(self, value):
        """
        Set the value of the MinCount input for this Choreo. ((optional, integer) Only returns results where mentions are at or above the supplied threshold.)
        """
        InputSet._set_input(self, 'MinCount', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) The page number to return.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Party(self, value):
        """
        Set the value of the Party input for this Choreo. ((optional, string) Limit results to members of congress from a given party. Valid values: R, D, I.)
        """
        InputSet._set_input(self, 'Party', value)
    def set_PerPage(self, value):
        """
        Set the value of the PerPage input for this Choreo. ((optional, integer) The number of results to return per page.)
        """
        InputSet._set_input(self, 'PerPage', value)
    def set_Phrase(self, value):
        """
        Set the value of the Phrase input for this Choreo. ((required, string) The phrase to search for.)
        """
        InputSet._set_input(self, 'Phrase', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) Output formats inlcude json and xml. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) The metric on which to sort top results. Acceptable inputs: tfidf or count. Defaults to tfidf.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((optional, string) Limit results to those on or after the given date. Format: YYYY-MM-DD)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Limit results to members from a particular state. Format: 2-letter state abbreviation (e.g. MD, RI, NY))
        """
        InputSet._set_input(self, 'State', value)

class TopPhraseSourcesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TopPhraseSources Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CapitolWords.)
        """
        return self._output.get('Response', None)

class TopPhraseSourcesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TopPhraseSourcesResultSet(response, path)
