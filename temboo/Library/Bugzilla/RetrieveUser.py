# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveUser
# Retrieve user info.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bugzilla/RetrieveUser')


    def new_input_set(self):
        return RetrieveUserInputSet()

    def _make_result_set(self, result, path):
        return RetrieveUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveUserChoreographyExecution(session, exec_id, path)

class RetrieveUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, password) Your Bugzilla password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_QueryUserID(self, value):
        """
        Set the value of the QueryUserID input for this Choreo. ((required, string) Enter the user ID for which information is to be returned. Valid input formats include: email address, or numeric user ID.  If searching by numeric ID, authentication is requred.)
        """
        InputSet._set_input(self, 'QueryUserID', value)
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

class RetrieveUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Bugzilla.)
        """
        return self._output.get('Response', None)

class RetrieveUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveUserResultSet(response, path)
