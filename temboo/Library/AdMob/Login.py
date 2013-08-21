# -*- coding: utf-8 -*-

###############################################################################
#
# Login
# Log into AdMob service and obtain an authorization token.
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
        Choreography.__init__(self, temboo_session, '/Library/AdMob/Login')


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
    def set_ClientKey(self, value):
        """
        Set the value of the ClientKey input for this Choreo. ((required, string) The Client Key provided by AdMob.)
        """
        InputSet._set_input(self, 'ClientKey', value)
    def set_Email(self, value):
        """
        Set the value of the Email input for this Choreo. ((required, string) Your AdMob username.)
        """
        InputSet._set_input(self, 'Email', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Admob password.)
        """
        InputSet._set_input(self, 'Password', value)

class LoginResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Login Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from AdMob in XML format)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((string) The token obtained by running this choreo.)
        """
        return self._output.get('Token', None)

class LoginChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LoginResultSet(response, path)
