# -*- coding: utf-8 -*-

###############################################################################
#
# SearchForUsers
# Search for a specified Bugzilla user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SearchForUsers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SearchForUsers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/SearchForUsers')


    def new_input_set(self):
        return SearchForUsersInputSet()

    def _make_result_set(self, result, path):
        return SearchForUsersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchForUsersChoreographyExecution(session, exec_id, path)

class SearchForUsersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SearchForUsers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Bugzilla password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SearchForUser(self, value):
        """
        Set the value of the SearchForUser input for this Choreo. ((required, string) Enter the usename to be querried.)
        """
        InputSet._set_input(self, 'SearchForUser', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        InputSet._set_input(self, 'Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Bugzilla username.)
        """
        InputSet._set_input(self, 'Username', value)

class SearchForUsersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SearchForUsers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class SearchForUsersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchForUsersResultSet(response, path)
