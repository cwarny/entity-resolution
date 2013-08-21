# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateFile
# Updates the content of an existing Google document.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/UpdateFile')


    def new_input_set(self):
        return UpdateFileInputSet()

    def _make_result_set(self, result, path):
        return UpdateFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateFileChoreographyExecution(session, exec_id, path)

class UpdateFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_FileContents(self, value):
        """
        Set the value of the FileContents input for this Choreo. ((conditional, string) The base64-encoded contents of the file you want to update.)
        """
        InputSet._set_input(self, 'FileContents', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((required, string) Enter the content type for the file. Currently, the supported content types are: application/pdf, application/rtf, application/msword, application/vnd.ms-excel, text/plain, and text/csv.)
        """
        InputSet._set_input(self, 'ContentType', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The password for your Google account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the document that you want to update.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The email address for your Google account.)
        """
        InputSet._set_input(self, 'Username', value)


class UpdateFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class UpdateFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateFileResultSet(response, path)
