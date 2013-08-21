# -*- coding: utf-8 -*-

###############################################################################
#
# SearchByKeyword
# Searches movie reviews by keyword and various filter parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchByKeyword(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchByKeyword Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/MovieReviews/SearchByKeyword')


    def new_input_set(self):
        return SearchByKeywordInputSet()

    def _make_result_set(self, result, path):
        return SearchByKeywordResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByKeywordChoreographyExecution(session, exec_id, path)

class SearchByKeywordInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchByKeyword
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
    def set_DVD(self, value):
        """
        Set the value of the DVD input for this Choreo. ((optional, string) Set this parameter to Y to limit the results to movies that have been released on DVD. To get only those movies that have not been released on DVD, specify N.)
        """
        InputSet._set_input(self, 'DVD', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of results to return.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) A numeric value indicating the starting point of the result set. This can be used in combination with the Limit input to page through results.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_OpeningDate(self, value):
        """
        Set the value of the OpeningDate input for this Choreo. ((optional, date) Limits by date or range of dates. The opening-date is the date the movie's opening date in the New York region. Format YYYY-MM-DD. Separate ranges with semicolons.)
        """
        InputSet._set_input(self, 'OpeningDate', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Sets the sort order of the results. Accepted values are: by-title, by-publication-date, by-opening-date, by-dvd-release-date.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_PublicationDate(self, value):
        """
        Set the value of the PublicationDate input for this Choreo. ((optional, date) Limits by date or range of dates. The publication-date is the date the review was first publish.ed in The Times. Format YYYY-MM-DD. Separate ranges with semicolons.)
        """
        InputSet._set_input(self, 'PublicationDate', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) A string of search keywords. Matches movie titles and indexed terms.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Reviewer(self, value):
        """
        Set the value of the Reviewer input for this Choreo. ((optional, string) Limits results to reviews by a specific critic. Reviewer names should be hyphenated or concatenated with dots (i.e manohla.dargis).)
        """
        InputSet._set_input(self, 'Reviewer', value)
    def set_ThousandBest(self, value):
        """
        Set the value of the ThousandBest input for this Choreo. ((optional, string) Set this parameter to Y to limit the results to movies on the Times list of The Best 1,000 Movies Ever Made. To get only those movies that are not on the list, specify N.)
        """
        InputSet._set_input(self, 'ThousandBest', value)

class SearchByKeywordResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchByKeyword Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the NY Times API.)
        """
        return self._output.get('Response', None)

class SearchByKeywordChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByKeywordResultSet(response, path)
