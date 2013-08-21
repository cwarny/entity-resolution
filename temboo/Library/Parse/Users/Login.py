# -*- coding: utf-8 -*-

###############################################################################
#
# Login
# Allows your application to authenticate a given user; returns user information, user-provided fields, and a session token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Login(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Login Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Users/Login')


    def new_input_set(self):
        return LoginInputSet()

    def _make_result_set(self, result, path):
        return LoginResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LoginChoreographyExecution(session, exec_id, path)

class LoginInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Login
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The password for the user that is loggin in.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The username for the user that is authenticating.)
        """
        InputSet._set_input(self, 'Username', value)

class LoginResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Login Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class LoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LoginResultSet(response, path)
