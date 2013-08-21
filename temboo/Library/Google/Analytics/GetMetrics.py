# -*- coding: utf-8 -*-

###############################################################################
#
# GetMetrics
# Retrieves metrics such as visits, page views, bounces within a specified time frame.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMetrics(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMetrics Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Analytics/GetMetrics')


    def new_input_set(self):
        return GetMetricsInputSet()

    def _make_result_set(self, result, path):
        return GetMetricsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMetricsChoreographyExecution(session, exec_id, path)

class GetMetricsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMetrics
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Dimensions(self, value):
        """
        Set the value of the Dimensions input for this Choreo. ((optional, string) Defines the primary data keys for your Analytics report. Use dimensions to segment your web property metrics (e.g.  ga:browser or ga:city).)
        """
        InputSet._set_input(self, 'Dimensions', value)
    def set_EndDate(self, value):
        """
        Set the value of the EndDate input for this Choreo. ((required, date) The end date for the range of data you want to retrieve. Epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        InputSet._set_input(self, 'EndDate', value)
    def set_Filters(self, value):
        """
        Set the value of the Filters input for this Choreo. ((optional, string) Restricts the data returned by a dimension or metric you want to filter by using an expression (i.e. ga:timeOnPage==10).)
        """
        InputSet._set_input(self, 'Filters', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The max results to be returned in the feed. Defaults to 50.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_Metrics(self, value):
        """
        Set the value of the Metrics input for this Choreo. ((optional, string) This is a comma separated list of metrics you want to retrieve. Defaults to: ga:visits,ga:bounces,ga:pageviews.)
        """
        InputSet._set_input(self, 'Metrics', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for your Google analytics account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProfileId(self, value):
        """
        Set the value of the ProfileId input for this Choreo. ((required, integer) The Google Analytics profile ID to access (this can be found under Profile Settings).)
        """
        InputSet._set_input(self, 'ProfileId', value)
    def set_Segment(self, value):
        """
        Set the value of the Segment input for this Choreo. ((optional, string) Used to segment your data by dimensions and/or metrics. You can use expressions for segments just as you would for the Filters parameter.)
        """
        InputSet._set_input(self, 'Segment', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Indicates the sorting order and direction for the returned data. Values can be separated by commas (i.e. ga:browser,ga:pageviews).)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_StartDate(self, value):
        """
        Set the value of the StartDate input for this Choreo. ((required, date) The start date for the range of data to retrieve. Use epoch timestamp in milliseconds or formatted as yyyy-MM-dd.)
        """
        InputSet._set_input(self, 'StartDate', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The starting entry for the feed. Defaults to 1.)
        """
        InputSet._set_input(self, 'StartIndex', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username for your Google analytics account.)
        """
        InputSet._set_input(self, 'Username', value)

class GetMetricsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMetrics Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Bounces(self):
        """
        Retrieve the value for the "Bounces" output from this Choreo execution. ((integer) The bounces metrics parsed from the Google Analytics response)
        """
        return self._output.get('Bounces', None)
    def get_PageViews(self):
        """
        Retrieve the value for the "PageViews" output from this Choreo execution. ((integer) The page views parsed from the Google Analytics response)
        """
        return self._output.get('PageViews', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The full response from Google Analytics.)
        """
        return self._output.get('Response', None)
    def get_Visits(self):
        """
        Retrieve the value for the "Visits" output from this Choreo execution. ((integer) The visits metrics parsed from the Google Analytics response.)
        """
        return self._output.get('Visits', None)

class GetMetricsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMetricsResultSet(response, path)
