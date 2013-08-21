# -*- coding: utf-8 -*-

###############################################################################
#
# GetReviewer
# Retrieves biographical information about reviewers.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetReviewer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetReviewer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/GetReviewer')


    def new_input_set(self):
        return GetReviewerInputSet()

    def _make_result_set(self, result, path):
        return GetReviewerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetReviewerChoreographyExecution(session, exec_id, path)

class GetReviewerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetReviewer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResourceType(self, value):
        """
        Set the value of the ResourceType input for this Choreo. ((optional, string) Specify "all", "full-time", or "part-time" for that subset. Specify a reviewer's name to get details about a reviewer. Names should be separated by hyphens or dots (i.e. manohla-dargis).)
        """
        InputSet._set_input(self, 'ResourceType', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetReviewerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetReviewer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class GetReviewerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetReviewerResultSet(response, path)
