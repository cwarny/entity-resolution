# -*- coding: utf-8 -*-

###############################################################################
#
# MoveFileOrFolder
# Moves a file or folder to a new location in the Dropbox tree.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Dropbox.DropboxItemMetadata import DropboxItemMetadata

import json

class MoveFileOrFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MoveFileOrFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Dropbox/FileOperations/MoveFileOrFolder')


    def new_input_set(self):
        return MoveFileOrFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveFileOrFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveFileOrFolderChoreographyExecution(session, exec_id, path)

class MoveFileOrFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MoveFileOrFolder
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
    def set_FromPath(self, value):
        """
        Set the value of the FromPath input for this Choreo. ((required, string) Specifies the file or folder to be copied.)
        """
        InputSet._set_input(self, 'FromPath', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Root(self, value):
        """
        Set the value of the Root input for this Choreo. ((conditional, string) The root relative to which path is specified. Valid values are "sandbox" and "dropbox" (the default). When your access token has the App folder level of access, this should be set to "sandbox".)
        """
        InputSet._set_input(self, 'Root', value)
    def set_ToPath(self, value):
        """
        Set the value of the ToPath input for this Choreo. ((required, string) Specifies the destination path, including the new name for the file or folder.)
        """
        InputSet._set_input(self, 'ToPath', value)

class MoveFileOrFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MoveFileOrFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Dropbox. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        return self._output.get('Response', None)
    def getItemMetadata(self):
        """
        The metadata for the file or folder being moved.
        """
        return DropboxItemMetadata(self.getJSONFromString(self._output.get('Response', [])))

class MoveFileOrFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveFileOrFolderResultSet(response, path)
