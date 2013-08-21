# -*- coding: utf-8 -*-

###############################################################################
#
# SearchAnonymous
# Allows anonymous users to search public forums.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchAnonymous(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchAnonymous Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Zendesk/Search/SearchAnonymous')


    def new_input_set(self):
        return SearchAnonymousInputSet()

    def _make_result_set(self, result, path):
        return SearchAnonymousResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchAnonymousChoreographyExecution(session, exec_id, path)

class SearchAnonymousInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchAnonymous
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) The email to authenticate the Zendesk account.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password matching the email to authenticate the Zendesk account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((required, string) Perform a search across usernames or email addresses.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((required, string) The server URL associated with your Zendesk account. In many cases this looks like: temboo.zendesk.com but may also be customized: support.temboo.com)
        """
        InputSet._set_input(self, 'Server', value)
    def set_SortBy(self, value):
        """
        Set the value of the SortBy input for this Choreo. ((optional, string) Acceptable values: updated_at, created_at, priority, status, ticket_type.)
        """
        InputSet._set_input(self, 'SortBy', value)
    def set_SortOrder(self, value):
        """
        Set the value of the SortOrder input for this Choreo. ((optional, string) Indicate either: relevance, asc (for ascending), desc (for descending). Defaults to relevance.)
        """
        InputSet._set_input(self, 'SortOrder', value)

class SearchAnonymousResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchAnonymous Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Zendesk.)
        """
        return self._output.get('Response', None)

class SearchAnonymousChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchAnonymousResultSet(response, path)
