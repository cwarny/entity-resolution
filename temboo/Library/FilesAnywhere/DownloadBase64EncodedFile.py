# -*- coding: utf-8 -*-

###############################################################################
#
# DownloadBase64EncodedFile
# Downloads a file from a specified directory in your FilesAnywhere account, and returns the content as Base64 encoded data.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DownloadBase64EncodedFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DownloadBase64EncodedFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/DownloadBase64EncodedFile')


    def new_input_set(self):
        return DownloadBase64EncodedFileInputSet()

    def _make_result_set(self, result, path):
        return DownloadBase64EncodedFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DownloadBase64EncodedFileChoreographyExecution(session, exec_id, path)

class DownloadBase64EncodedFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DownloadBase64EncodedFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((conditional, string) The API Key provided by FilesAnywhere. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((conditional, password) Your FilesAnywhere password. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((required, string) The path to the file you want to download (i.e. \JOHNSMITH\MyFolder\MyFile.txt).)
        """
        InputSet._set_input(self, 'Path', value)
    def set_Token(self, value):
        """
        Set the value of the Token input for this Choreo. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        InputSet._set_input(self, 'Token', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((conditional, string) Your FilesAnywhere username. Required unless supplying a valid Token input.)
        """
        InputSet._set_input(self, 'Username', value)

class DownloadBase64EncodedFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DownloadBase64EncodedFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from FilesAnywhere. The response contains the Base64 encoded content of the file you are downloading.)
        """
        return self._output.get('Response', None)
    def get_Token(self):
        """
        Retrieve the value for the "Token" output from this Choreo execution. ((conditional, string) If provided, the Choreo will use the token to authenticate. If the token is expired or not provided, the Choreo will relogin and retrieve a new token when APIKey, Username, and Password are supplied.)
        """
        return self._output.get('Token', None)

class DownloadBase64EncodedFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DownloadBase64EncodedFileResultSet(response, path)
