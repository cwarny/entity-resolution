# -*- coding: utf-8 -*-

###############################################################################
#
# ListIssuesForRepo
# List all issues for a specified repository.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListIssuesForRepo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListIssuesForRepo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/IssuesAPI/Issues/ListIssuesForRepo')


    def new_input_set(self):
        return ListIssuesForRepoInputSet()

    def _make_result_set(self, result, path):
        return ListIssuesForRepoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListIssuesForRepoChoreographyExecution(session, exec_id, path)

class ListIssuesForRepoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListIssuesForRepo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Assignee(self, value):
        """
        Set the value of the Assignee input for this Choreo. ((required, string) Can be set to a username, "none" for issues with no assinged user, or * for issues with any assigned user.)
        """
        InputSet._set_input(self, 'Assignee', value)
    def set_Direction(self, value):
        """
        Set the value of the Direction input for this Choreo. ((optional, string) The direction of the sort order. Valid values are: asc or desc (the default).)
        """
        InputSet._set_input(self, 'Direction', value)
    def set_Labels(self, value):
        """
        Set the value of the Labels input for this Choreo. ((optional, string) A comma separated list of label names (i.e. bug, ui, etc).)
        """
        InputSet._set_input(self, 'Labels', value)
    def set_Mentioned(self, value):
        """
        Set the value of the Mentioned input for this Choreo. ((optional, string) A Github username that is mentioned.)
        """
        InputSet._set_input(self, 'Mentioned', value)
    def set_Milestone(self, value):
        """
        Set the value of the Milestone input for this Choreo. ((required, string) Can be set to a milestone number, "none" for issues with no milestone, or * for issues with any milestone.)
        """
        InputSet._set_input(self, 'Milestone', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Indicates the page index that you want to retrieve. This is used to page through many results. Defaults to 1.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repo.)
        """
        InputSet._set_input(self, 'Repo', value)
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
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) A GitHub username.)
        """
        InputSet._set_input(self, 'User', value)

class ListIssuesForRepoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListIssuesForRepo Choreo.
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

class ListIssuesForRepoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListIssuesForRepoResultSet(response, path)
