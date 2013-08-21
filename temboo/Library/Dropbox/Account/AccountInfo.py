# -*- coding: utf-8 -*-

###############################################################################
#
# AccountInfo
# Retrieves information about the user's account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Dropbox.DropboxAccountInfo import DropboxAccountInfo

import json

class AccountInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AccountInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/Account/AccountInfo')


    def new_input_set(self):
        return AccountInfoInputSet()

    def _make_result_set(self, result, path):
        return AccountInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AccountInfoChoreographyExecution(session, exec_id, path)

class AccountInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AccountInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
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
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The App Key provided by Dropbox (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The App Secret provided by Dropbox (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'AppSecret', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class AccountInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AccountInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)
    def getAccountInfo(self):
        """
        Information about the user's account.
        """
        return DropboxAccountInfo(self.getJSONFromString(self._output.get('Response', [])))

class AccountInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AccountInfoResultSet(response, path)
