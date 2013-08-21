# -*- coding: utf-8 -*-

###############################################################################
#
# ZipFile
# Creates a zipped version of the specified Box file and returns a link to the new compressed file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ZipFile(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipFile Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Files/ZipFile')


    def new_input_set(self):
        return ZipFileInputSet()

    def _make_result_set(self, result, path):
        return ZipFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipFileChoreographyExecution(session, exec_id, path)

class ZipFileInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipFile
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The id of the file to zip.)
        """
        InputSet._set_input(self, 'FileID', value)
    def set_SharedLink(self, value):
        """
        Set the value of the SharedLink input for this Choreo. ((conditional, json) A JSON object  representing the item’s shared link and associated permissions. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'SharedLink', value)
    def set_ZipFileLocation(self, value):
        """
        Set the value of the ZipFileLocation input for this Choreo. ((conditional, string) The id of the folder to put the new zip file in. When not specified, the zip file will be put in the root folder.)
        """
        InputSet._set_input(self, 'ZipFileLocation', value)
    def set_ZipFileName(self, value):
        """
        Set the value of the ZipFileName input for this Choreo. ((required, string) The name of the zip file that will be created.)
        """
        InputSet._set_input(self, 'ZipFileName', value)


class ZipFileResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipFile Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from Box. This contains the newly created zip file metadata.)
        """
        return self._output.get('Response', None)
    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The url for the newly created zip file.)
        """
        return self._output.get('URL', None)

class ZipFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ZipFileResultSet(response, path)
