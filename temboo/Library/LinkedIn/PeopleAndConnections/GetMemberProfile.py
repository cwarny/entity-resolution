# -*- coding: utf-8 -*-

###############################################################################
#
# GetMemberProfile
# Returns the standard default profile of the current user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetMemberProfile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetMemberProfile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/LinkedIn/PeopleAndConnections/GetMemberProfile')


    def new_input_set(self):
        return GetMemberProfileInputSet()

    def _make_result_set(self, result, path):
        return GetMemberProfileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetMemberProfileChoreographyExecution(session, exec_id, path)

class GetMemberProfileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetMemberProfile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by LinkedIn (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by LinkedIn (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)

class GetMemberProfileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetMemberProfile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from LinkedIn in XML format.)
        """
        return self._output.get('Response', None)

class GetMemberProfileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetMemberProfileResultSet(response, path)
