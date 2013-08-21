# -*- coding: utf-8 -*-

###############################################################################
#
# UnfollowUser
# List posts made by a user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UnfollowUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UnfollowUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/UnfollowUser')


    def new_input_set(self):
        return UnfollowUserInputSet()

    def _make_result_set(self, result, path):
        return UnfollowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UnfollowUserChoreographyExecution(session, exec_id, path)

class UnfollowUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UnfollowUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default), jsonp, or rss.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The User ID that is to be unfollowed. If UserID is set, then Username must be null.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) A Disqus username.  If Username is being set, then UserID must be null.)
        """
        InputSet._set_input(self, 'Username', value)

class UnfollowUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UnfollowUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Disqus.)
        """
        return self._output.get('Response', None)

class UnfollowUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UnfollowUserResultSet(response, path)
