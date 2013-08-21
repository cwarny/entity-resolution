# -*- coding: utf-8 -*-

###############################################################################
#
# FollowUser
# Follows the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FollowUser(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FollowUser Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/FollowUser')


    def new_input_set(self):
        return FollowUserInputSet()

    def _make_result_set(self, result, path):
        return FollowUserResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FollowUserChoreographyExecution(session, exec_id, path)

class FollowUserInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FollowUser
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) A valid OAuth 2.0 access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) The name of a callback function to wrap the respone in. Used when setting ResponseFormat to "jsonp".)
        """
        InputSet._set_input(self, 'Callback', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and jsonp.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The User ID that is to be followed. If UserID is set, then Username must be null.)
        """
        InputSet._set_input(self, 'UserID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) The Disqus username that is to be followed.  If Username is being set, then UserID must be null.)
        """
        InputSet._set_input(self, 'Username', value)


class FollowUserResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FollowUser Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class FollowUserChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FollowUserResultSet(response, path)
