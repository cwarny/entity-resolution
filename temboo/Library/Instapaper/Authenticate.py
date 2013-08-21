# -*- coding: utf-8 -*-

###############################################################################
#
# Authenticate
# Validate an Instapaper account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Authenticate(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Authenticate Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instapaper/Authenticate')


    def new_input_set(self):
        return AuthenticateInputSet()

    def _make_result_set(self, result, path):
        return AuthenticateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AuthenticateChoreographyExecution(session, exec_id, path)

class AuthenticateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Authenticate
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Your Instapaper password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Instapaper username.)
        """
        InputSet._set_input(self, 'Username', value)

class AuthenticateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Authenticate Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Instapaper. Successful reqests will return a 200 status code.)
        """
        return self._output.get('Response', None)

class AuthenticateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AuthenticateResultSet(response, path)
