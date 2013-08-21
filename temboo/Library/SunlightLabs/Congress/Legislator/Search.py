# -*- coding: utf-8 -*-

###############################################################################
#
# Search
# Provides a fuzzy-matching text search of the legislators.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Search(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Search Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/SunlightLabs/Congress/Legislator/Search')


    def new_input_set(self):
        return SearchInputSet()

    def _make_result_set(self, result, path):
        return SearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchChoreographyExecution(session, exec_id, path)

class SearchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Search
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Sunlight Labs.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AllLegislators(self, value):
        """
        Set the value of the AllLegislators input for this Choreo. ((optional, boolean) A boolean flag indicating to search for all legislators even when they are no longer in office.)
        """
        InputSet._set_input(self, 'AllLegislators', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((required, string) A name to search for.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class SearchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Search Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the Sunlight Congress API.)
        """
        return self._output.get('Response', None)

class SearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchResultSet(response, path)
