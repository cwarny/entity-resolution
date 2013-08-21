# -*- coding: utf-8 -*-

###############################################################################
#
# FinalizeOAuth
# Completes the OAuth 2 process by retrieving a Disqus access token, refresh token, expiration time for the access token, username and user ID, after they have visited the authorization URL returned by the InitializeOAuth choreo and clicked "allow."
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FinalizeOAuth(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FinalizeOAuth Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Disqus/OAuth/FinalizeOAuth')


    def new_input_set(self):
        return FinalizeOAuthInputSet()

    def _make_result_set(self, result, path):
        return FinalizeOAuthResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FinalizeOAuthChoreographyExecution(session, exec_id, path)

class FinalizeOAuthInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FinalizeOAuth
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) Your Temboo account name.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_AppKeyName(self, value):
        """
        Set the value of the AppKeyName input for this Choreo. ((required, string) The name of your Temboo application key.)
        """
        InputSet._set_input(self, 'AppKeyName', value)
    def set_AppKeyValue(self, value):
        """
        Set the value of the AppKeyValue input for this Choreo. ((required, string) Your Temboo application key.)
        """
        InputSet._set_input(self, 'AppKeyValue', value)
    def set_CallbackID(self, value):
        """
        Set the value of the CallbackID input for this Choreo. ((required, string) The callback token returned by the InitializeOAuth Choreo. Used to retrieve the authorization code after the user authorizes.)
        """
        InputSet._set_input(self, 'CallbackID', value)
    def set_PublicKey(self, value):
        """
        Set the value of the PublicKey input for this Choreo. ((required, string) The Public Key provided by Disqus (AKA the API Key).)
        """
        InputSet._set_input(self, 'PublicKey', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Disqus (AKA the API Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, integer) The amount of time (in seconds) to poll your Temboo callback URL to see if your app's user has allowed or denied the request for access. Defaults to 20. Max is 60.)
        """
        InputSet._set_input(self, 'Timeout', value)

class FinalizeOAuthResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FinalizeOAuth Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_AccessToken(self):
        """
        Retrieve the value for the "AccessToken" output from this Choreo execution. ((string) The Access Token for the user that has granted access to your application.)
        """
        return self._output.get('AccessToken', None)
    def get_Expires(self):
        """
        Retrieve the value for the "Expires" output from this Choreo execution. ((integer) The expiration time in seconds of the access token retrieved.)
        """
        return self._output.get('Expires', None)
    def get_RefreshToken(self):
        """
        Retrieve the value for the "RefreshToken" output from this Choreo execution. ((string) A valid refresh token used to generate a new access token.)
        """
        return self._output.get('RefreshToken', None)
    def get_UserID(self):
        """
        Retrieve the value for the "UserID" output from this Choreo execution. ((string) The Disqus User ID associated with the access token.)
        """
        return self._output.get('UserID', None)
    def get_Username(self):
        """
        Retrieve the value for the "Username" output from this Choreo execution. ((string) The Disqus Username associated with the access token.)
        """
        return self._output.get('Username', None)

class FinalizeOAuthChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FinalizeOAuthResultSet(response, path)
