# -*- coding: utf-8 -*-

###############################################################################
#
# SearchWithinBoundedBox
# Allows you to do a spatial search for events within a box bounded by specified northeast and southwest points.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchWithinBoundedBox(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchWithinBoundedBox Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/EventListings/SearchWithinBoundedBox')


    def new_input_set(self):
        return SearchWithinBoundedBoxInputSet()

    def _make_result_set(self, result, path):
        return SearchWithinBoundedBoxResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchWithinBoundedBoxChoreographyExecution(session, exec_id, path)

class SearchWithinBoundedBoxInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchWithinBoundedBox
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
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_NortheastLatitude(self, value):
        """
        Set the value of the NortheastLatitude input for this Choreo. ((conditional, decimal) The northeastern latitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        InputSet._set_input(self, 'NortheastLatitude', value)
    def set_NortheastLongitude(self, value):
        """
        Set the value of the NortheastLongitude input for this Choreo. ((conditional, decimal) The northeastern longitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        InputSet._set_input(self, 'NortheastLongitude', value)
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
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to json, xml, or sphp. Defaults to xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Allows you to sort results. Appending "+asc" or "+desc" to a facet will sort results on that value in ascending or descending order (i.e. dist+asc).)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_SouthwestLatitude(self, value):
        """
        Set the value of the SouthwestLatitude input for this Choreo. ((conditional, decimal) The southwest latitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        InputSet._set_input(self, 'SouthwestLatitude', value)
    def set_SouthwestLongitude(self, value):
        """
        Set the value of the SouthwestLongitude input for this Choreo. ((conditional, decimal) The southwest longitude of the bounding box to search. When searching within a bounded box, all four coordinates are required.)
        """
        InputSet._set_input(self, 'SouthwestLongitude', value)

class SearchWithinBoundedBoxResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchWithinBoundedBox Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API. Valid values are: json (the default) and xml.)
        """
        return self._output.get('Response', None)

class SearchWithinBoundedBoxChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchWithinBoundedBoxResultSet(response, path)
