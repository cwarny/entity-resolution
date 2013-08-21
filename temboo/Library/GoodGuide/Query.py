# -*- coding: utf-8 -*-

###############################################################################
#
# Query
# Queries the GoodGuide API by keyword and retrieves information on GoodGuide products.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Query(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Query Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GoodGuide/Query')


    def new_input_set(self):
        return QueryInputSet()

    def _make_result_set(self, result, path):
        return QueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryChoreographyExecution(session, exec_id, path)

class QueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Query
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIFormat(self, value):
        """
        Set the value of the APIFormat input for this Choreo. ((optional, string) The response type supplied by GoodGuides. Default is reference. Other acceptable inputs are simple and badge.)
        """
        InputSet._set_input(self, 'APIFormat', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by GoodGuide.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) The number of entries to return. Default is 20. Up to 50 entries can be returned at once.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) A text string used in the keyword search. By default, queries return product data only. Use the EntityType input to query other types of entities.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Acceptable values: best_match (for keyword searches, this is the default); rating (the overall GoodGuide rating); and name (sorted alphabetically).)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Acceptable values: 'desc' to sort descending (default for sort_by=rating and sort_by is best_match); 'asc' to sort ascending (default for sort_by is name).)
        """
        InputSet._set_input(self, 'SortOrder', value)

class QueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Query Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from GoodGuide.)
        """
        return self._output.get('Response', None)

class QueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryResultSet(response, path)
