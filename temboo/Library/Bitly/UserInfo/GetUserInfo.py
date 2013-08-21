# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserInfo
# Returns information about a specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUserInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bitly/UserInfo/GetUserInfo')


    def new_input_set(self):
        return GetUserInfoInputSet()

    def _make_result_set(self, result, path):
        return GetUserInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserInfoChoreographyExecution(session, exec_id, path)

class GetUserInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_FullName(self, value):
        """
        Set the value of the FullName input for this Choreo. ((optional, string) The users full name value (only available for the authenticated user).)
        """
        InputSet._set_input(self, 'FullName', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((optional, string) The bitly login of the user whose info to look up. If not given, the authenticated user will be used.)
        """
        InputSet._set_input(self, 'Login', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Accepted values are "json" or "xml". Defaults to "json".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetUserInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class GetUserInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserInfoResultSet(response, path)
