# -*- coding: utf-8 -*-

###############################################################################
#
# GetNewsItem
# Queries the Newswire API for a specific news item.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetNewsItem(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetNewsItem Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/TimesNewswire/GetNewsItem')


    def new_input_set(self):
        return GetNewsItemInputSet()

    def _make_result_set(self, result, path):
        return GetNewsItemResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetNewsItemChoreographyExecution(session, exec_id, path)

class GetNewsItemInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetNewsItem
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The complete URL of a specific news item. This URL is returned in the output of the GetRecentNews Choreo.)
        """
        InputSet._set_input(self, 'URL', value)

class GetNewsItemResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetNewsItem Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetNewsItemChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetNewsItemResultSet(response, path)
