# -*- coding: utf-8 -*-

###############################################################################
#
# ZipFolder
# Creates a zip file containing all files within the specified folder and returns a link to the new compressed file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ZipFolder(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ZipFolder Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/ZipFolder')


    def new_input_set(self):
        return ZipFolderInputSet()

    def _make_result_set(self, result, path):
        return ZipFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ZipFolderChoreographyExecution(session, exec_id, path)

class ZipFolderInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ZipFolder
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((conditional, string) The id of the folder that you want to retrieve items for to zip. To indicate the root folder, specify 0.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_SharedLink(self, value):
        """
        Set the value of the SharedLink input for this Choreo. ((conditional, json) A JSON object  representing the item’s shared link and associated permissions. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'SharedLink', value)
    def set_ZipFileLocation(self, value):
        """
        Set the value of the ZipFileLocation input for this Choreo. ((optional, string) The id of the folder to put the new zip file in. When not specified, the zip file will be put in the root folder.)
        """
        InputSet._set_input(self, 'ZipFileLocation', value)
    def set_ZipFileName(self, value):
        """
        Set the value of the ZipFileName input for this Choreo. ((required, string) The name of the zip file that will be created.)
        """
        InputSet._set_input(self, 'ZipFileName', value)


class ZipFolderResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ZipFolder Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box. This contains the newly created zip file metadata.)
        """
        return self._output.get('Response', None)
    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The url for the newly created zip file.)
        """
        return self._output.get('URL', None)

class ZipFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ZipFolderResultSet(response, path)
