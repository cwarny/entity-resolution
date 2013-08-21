# -*- coding: utf-8 -*-

###############################################################################
#
# Upload
# Upload a file to RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Upload(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Upload Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/Upload')


    def new_input_set(self):
        return UploadInputSet()

    def _make_result_set(self, result, path):
        return UploadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadChoreographyExecution(session, exec_id, path)

class UploadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Upload
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((conditional, string) The base64 encoded contents of the file you want to upload. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The name of the file you want to upload)
        """
        InputSet._set_input(self, 'FileName', value)
    def set_Folder(self, value):
        """
        Set the value of the Folder input for this Choreo. ((optional, integer) The id of the folder you want to upload the file to)
        """
        InputSet._set_input(self, 'Folder', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)


class UploadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Upload Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare formatted in commas separated values.)
        """
        return self._output.get('Response', None)

class UploadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadResultSet(response, path)
