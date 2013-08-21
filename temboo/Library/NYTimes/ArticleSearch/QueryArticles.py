# -*- coding: utf-8 -*-

###############################################################################
#
# QueryArticles
# Lets you query the Article Search API for New York Times articles.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.NYTimes.NYTimesArticle import NYTimesArticle

import json

class QueryArticles(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the QueryArticles Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/ArticleSearch/QueryArticles')


    def new_input_set(self):
        return QueryArticlesInputSet()

    def _make_result_set(self, result, path):
        return QueryArticlesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return QueryArticlesChoreographyExecution(session, exec_id, path)

class QueryArticlesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the QueryArticles
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_BeginDate(self, value):
        """
        Set the value of the BeginDate input for this Choreo. ((optional, date) Sets the starting point (which is inclusive) of the range of publication dates to return. Must be used with EndDate. Date should be formatted like YYYYMMDD.)
        """
        InputSet._set_input(self, 'BeginDate', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((optional, date) Sets the end point (which is inclusive) of the range of publication dates to return. Must be used with BeginDate. Date should be formatted like YYYYMMDD.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Facets(self, value):
        """
        Set the value of the Facets input for this Choreo. ((optional, string) A comma-delimited list of up to 5 facets. This indicates the sets of facet values to include in the response. See Choreo documentation for more information about accepted values for this input.)
        """
        InputSet._set_input(self, 'Facets', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-delimited list of fields to return. These fields are returned by default: body, byline, date, title, and url.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) This corresponds to which set of 10 results is returned. Used to page through results. Set to 0 to return records 0-9, set to 1 to return records 10-19, etc.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Search keywords (optionally applied to specific fields) and/or facets. See Choreo documentation for syntax examples.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Rank(self, value):
        """
        Set the value of the Rank input for this Choreo. ((optional, string) Sets the order of the results. Accepted values are: newest (the defaults), oldest, or closest.)
        """
        InputSet._set_input(self, 'Rank', value)

class QueryArticlesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the QueryArticles Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from the NY Times API.)
        """
        return self._output.get('Response', None)
    def getOffset(self):
        """
        The value of offset corresponds to a set of 10 results (i.e. offset=0 for results 0-9, offset=1 for results 10-19, etc)
        """
        return self.getJSONFromString(self._output.get('Response', [])).get("offset", [])
    def getArticles(self):
        """
        Get an article matching the search criteria
        """
        return [NYTimesArticle(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("results", [])]

    def getTokens(self):
        """
        Contains the search tokens provided for the query
        """
        return [le for le in self.getJSONFromString(self._output.get('Response', [])).get("tokens", [])]

    def getTotal(self):
        """
        The total number of articles for this search
        """
        return self.getJSONFromString(self._output.get('Response', [])).get("total", [])

class QueryArticlesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return QueryArticlesResultSet(response, path)
