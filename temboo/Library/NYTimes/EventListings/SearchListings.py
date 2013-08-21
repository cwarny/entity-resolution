# -*- coding: utf-8 -*-

###############################################################################
#
# SearchListings
# Searches events by location, filters, or full text search.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchListings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchListings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/EventListings/SearchListings')


    def new_input_set(self):
        return SearchListingsInputSet()

    def _make_result_set(self, result, path):
        return SearchListingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchListingsChoreographyExecution(session, exec_id, path)

class SearchListingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchListings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_DateRange(self, value):
        """
        Set the value of the DateRange input for this Choreo. ((optional, date) Start date to end date in the following format: YYYY-MM-DD:YYYY-MM-DD.)
        """
        InputSet._set_input(self, 'DateRange', value)
    def set_Filters(self, value):
        """
        Set the value of the Filters input for this Choreo. ((optional, string) Filters search results using facet names and values. See Choreo documentation for examples.)
        """
        InputSet._set_input(self, 'Filters', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((optional, decimal) The latitude coordinate of the location to use in the event search. If specified, Longitude must also be provided.)
        """
        InputSet._set_input(self, 'Latitude', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((optional, decimal) The longitude coordinate of the location to use in the event search. If specified, Latitude must also be provided.)
        """
        InputSet._set_input(self, 'Longitude', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((optional, string) Search keywords to perform a text search on the following fields: web_description, event_name and venue_name.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Radius(self, value):
        """
        Set the value of the Radius input for this Choreo. ((optional, integer) The radius of the spacial search (in meters). Defaults to 1000.)
        """
        InputSet._set_input(self, 'Radius', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Allows you to sort results. Appending "+asc" or "+desc" to a facet will sort results on that value in ascending or descending order (i.e. dist+asc).)
        """
        InputSet._set_input(self, 'Sort', value)

class SearchListingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchListings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API. Format corresponds to the ResponseFormat input. Defaults to xml.)
        """
        return self._output.get('Response', None)

class SearchListingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchListingsResultSet(response, path)
