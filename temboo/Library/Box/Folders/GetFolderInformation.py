# -*- coding: utf-8 -*-

###############################################################################
#
# GetFolderInformation
# Retrieves information for a specified folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetFolderInformation(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFolderInformation Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Folders/GetFolderInformation')


    def new_input_set(self):
        return GetFolderInformationInputSet()

    def _make_result_set(self, result, path):
        return GetFolderInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFolderInformationChoreographyExecution(session, exec_id, path)

class GetFolderInformationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFolderInformation
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FolderID(self, value):
        """
        Set the value of the FolderID input for this Choreo. ((conditional, string) The id of the folder that you want to retrieve information for. Defaults to 0 indicating the "root" folder.)
        """
        InputSet._set_input(self, 'FolderID', value)


class GetFolderInformationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFolderInformation Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class GetFolderInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFolderInformationResultSet(response, path)
