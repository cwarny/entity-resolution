# -*- coding: utf-8 -*-

###############################################################################
#
# ListYourIssues
# Lists all issues associated with the provided access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListYourIssues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListYourIssues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/IssuesAPI/Issues/ListYourIssues')


    def new_input_set(self):
        return ListYourIssuesInputSet()

    def _make_result_set(self, result, path):
        return ListYourIssuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListYourIssuesChoreographyExecution(session, exec_id, path)

class ListYourIssuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListYourIssues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Direction(self, value):
        """
        Set the value of the Direction input for this Choreo. ((optional, string) The direction of the sort order. Valid values are: asc or desc (the default).)
        """
        InputSet._set_input(self, 'Direction', value)
    def set_Filter(self, value):
        """
        Set the value of the Filter input for this Choreo. ((optional, string) Filters issues using one of the following strings: assigned (the default), created, mentioned, subscribed.)
        """
        InputSet._set_input(self, 'Filter', value)
    def set_Labels(self, value):
        """
        Set the value of the Labels input for this Choreo. ((optional, string) A comma separated list of label names (i.e. bug, ui, etc).)
        """
        InputSet._set_input(self, 'Labels', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Since(self, value):
        """
        Set the value of the Since input for this Choreo. ((optional, date) A timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ). Returns issues since this date.)
        """
        InputSet._set_input(self, 'Since', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Indicates how the issues will be sorted in the response. Valid sort options are: created (the default), updated, comments.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_State(self, value):
        """
        Set the value of the State input for this Choreo. ((optional, string) Returns issues with a particular state: open (the default) or closed.)
        """
        InputSet._set_input(self, 'State', value)

class ListYourIssuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListYourIssues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_LastPage(self):
        """
        Retrieve the value for the "LastPage" output from this Choreo execution. ((integer) If multiple pages are available for the response, this contains the last available page.)
        """
        return self._output.get('LastPage', None)
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_NextPage(self):
        """
        Retrieve the value for the "NextPage" output from this Choreo execution. ((integer) If multiple pages are available for the response, this contains the next page that you should retrieve.)
        """
        return self._output.get('NextPage', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)

class ListYourIssuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListYourIssuesResultSet(response, path)
