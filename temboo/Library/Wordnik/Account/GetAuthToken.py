# -*- coding: utf-8 -*-

###############################################################################
#
# GetAuthToken
# Obtains an authentication token for use in other Wordnik Choreos.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAuthToken(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAuthToken Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetAuthToken')


    def new_input_set(self):
        return GetAuthTokenInputSet()

    def _make_result_set(self, result, path):
        return GetAuthTokenResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAuthTokenChoreographyExecution(session, exec_id, path)

class GetAuthTokenInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAuthToken
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) Password of the Wordnik account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Username of the Wordnik account.)
        """
        InputSet._set_input(self, 'Username', value)

class GetAuthTokenResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAuthToken Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. (The Token obtained from running this Choreo.)
        """
        return self._output.get('Token', None)

class GetAuthTokenChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAuthTokenResultSet(response, path)
