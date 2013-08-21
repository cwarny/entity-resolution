# -*- coding: utf-8 -*-

###############################################################################
#
# Account
# Retrieves the account information for the user associated with the given authorized access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Account(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Account Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dwolla/Users/Account')


    def new_input_set(self):
        return AccountInputSet()

    def _make_result_set(self, result, path):
        return AccountResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountChoreographyExecution(session, exec_id, path)

class AccountInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Account
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth token.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class AccountResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Account Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dwolla.)
        """
        return self._output.get('Response', None)

class AccountChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountResultSet(response, path)
