# -*- coding: utf-8 -*-

###############################################################################
#
# SetFile
# Allows you to update or create a file on the CloudMine server.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class SetFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SetFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/FileStorage/SetFile')


    def new_input_set(self):
        return SetFileInputSet()

    def _make_result_set(self, result, path):
        return SetFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetFileChoreographyExecution(session, exec_id, path)

class SetFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SetFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) The Content-Type of the file you are creating or updating. This defaults to application/octet-stream.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((conditional, string) The Base64 encoded contents of the file.)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_Key(self, value):
        """
        Set the value of the Key input for this Choreo. ((optional, string) A key for the file you are uploading. If provided, the file will be stored with this key; otherwise, a key will be generated and returned.)
        """
        InputSet._set_input(self, 'Key', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        InputSet._set_input(self, 'SessionToken', value)


class SetFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SetFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class SetFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetFileResultSet(response, path)
