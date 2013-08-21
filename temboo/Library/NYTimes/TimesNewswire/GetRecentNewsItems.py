# -*- coding: utf-8 -*-

###############################################################################
#
# GetRecentNewsItems
# Retrieves recent news items.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetRecentNewsItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetRecentNewsItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/TimesNewswire/GetRecentNewsItems')


    def new_input_set(self):
        return GetRecentNewsItemsInputSet()

    def _make_result_set(self, result, path):
        return GetRecentNewsItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetRecentNewsItemsChoreographyExecution(session, exec_id, path)

class GetRecentNewsItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetRecentNewsItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return. Defaults to 20.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Section(self, value):
        """
        Set the value of the Section input for this Choreo. ((optional, string) Limits the set of items by one or more sections. Separate sections by semicolons. Defaults to "all" to get all sections. See Choreo documentation for more options for this input.)
        """
        InputSet._set_input(self, 'Section', value)
    def set_Source(self, value):
        """
        Set the value of the Source input for this Choreo. ((optional, string) Limits the set of items by originating source. Set to "nyt" for New York Times items only and "iht" for International Herald Tribune items. Set to "all" for both (the default).)
        """
        InputSet._set_input(self, 'Source', value)
    def set_TimePeriod(self, value):
        """
        Set the value of the TimePeriod input for this Choreo. ((optional, integer) Limits the set of items by time published. Valid range is number of hours, 1–720 (in hours). Defaults to 24.)
        """
        InputSet._set_input(self, 'TimePeriod', value)

class GetRecentNewsItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetRecentNewsItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetRecentNewsItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetRecentNewsItemsResultSet(response, path)
