# -*- coding: utf-8 -*-

###############################################################################
#
# CheckUsername
# Check whether the provided username is available.  An error is returned if the entered username is either taken, or invalid.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CheckUsername(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CheckUsername Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/Users/CheckUsername')


    def new_input_set(self):
        return CheckUsernameInputSet()

    def _make_result_set(self, result, path):
        return CheckUsernameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CheckUsernameChoreographyExecution(session, exec_id, path)

class CheckUsernameInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CheckUsername
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
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Enter a Disqus username.)
        """
        InputSet._set_input(self, 'Username', value)


class CheckUsernameResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CheckUsername Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Disqus.)
        """
        return self._output.get('Response', None)

class CheckUsernameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CheckUsernameResultSet(response, path)
