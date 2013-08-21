# -*- coding: utf-8 -*-

###############################################################################
#
# ListBugHistory
# Retrieve detailed bug history.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListBugHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListBugHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/ListBugHistory')


    def new_input_set(self):
        return ListBugHistoryInputSet()

    def _make_result_set(self, result, path):
        return ListBugHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBugHistoryChoreographyExecution(session, exec_id, path)

class ListBugHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListBugHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_BugID(self, value):
        """
        Set the value of the BugID input for this Choreo. ((required, integer) Enter a Bug ID, for which information will be retrieved.)
        """
        InputSet._set_input(self, 'BugID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Server(self, value):
        """
        Set the value of the Server input for this Choreo. ((optional, string) The base URL for the Bugzilla server to access. Defaults to https://api-dev.bugzilla.mozilla.org/latest. To access the test server, set to https://api-dev.bugzilla.mozilla.org/test/latest.)
        """
        InputSet._set_input(self, 'Server', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) Your Bugzilla username.)
        """
        InputSet._set_input(self, 'Username', value)

class ListBugHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListBugHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class ListBugHistoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBugHistoryResultSet(response, path)
