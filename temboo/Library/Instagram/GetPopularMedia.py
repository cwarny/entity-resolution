# -*- coding: utf-8 -*-

###############################################################################
#
# GetPopularMedia
# Retrieves a list of what media is most popular at the moment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPopularMedia(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPopularMedia Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetPopularMedia')


    def new_input_set(self):
        return GetPopularMediaInputSet()

    def _make_result_set(self, result, path):
        return GetPopularMediaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPopularMediaChoreographyExecution(session, exec_id, path)

class GetPopularMediaInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPopularMedia
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The access token retrieved during the OAuth 2.0 process. Required unless you provide the ClientID.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Instagram after registering your application. Required unless you provide the AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)

class GetPopularMediaResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPopularMedia Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetPopularMediaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPopularMediaResultSet(response, path)
