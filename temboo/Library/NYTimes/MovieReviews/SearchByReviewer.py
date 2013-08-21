# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByReviewer
# Retrieves reviews by a specific Times reviewer.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByReviewer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByReviewer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/SearchByReviewer')


    def new_input_set(self):
        return SearchByReviewerInputSet()

    def _make_result_set(self, result, path):
        return SearchByReviewerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByReviewerChoreographyExecution(session, exec_id, path)

class SearchByReviewerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByReviewer
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by NY Times.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_CriticsPick(self, value):
        """
        Set the value of the CriticsPick input for this Choreo. ((optional, string) Set this parameter to Y to limt the results to NYT Critics' Picks. To get only those movies that have not been highlighted by Times critics, specify N.)
        """
        InputSet._set_input(self, 'CriticsPick', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) A numeric value indicating the starting point of the result set. Used to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Sets the sort order of the results. Accepted values are: by-title, by-publication-date, by-opening-date, by-dvd-release-date.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ReviewerName(self, value):
        """
        Set the value of the ReviewerName input for this Choreo. ((required, string) The name of the Times reviewer. Reviewer names should be separated by hyphens or dots (i.e. manohla-dargis or manohla.dargis).)
        """
        InputSet._set_input(self, 'ReviewerName', value)

class SearchByReviewerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByReviewer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class SearchByReviewerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByReviewerResultSet(response, path)
