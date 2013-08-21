# -*- coding: utf-8 -*-

###############################################################################
#
# GetContents
# Returns a tarball or zipball archive for a repository. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetContents(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetContents Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/ReposAPI/Contents/GetContents')


    def new_input_set(self):
        return GetContentsInputSet()

    def _make_result_set(self, result, path):
        return GetContentsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetContentsChoreographyExecution(session, exec_id, path)

class GetContentsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetContents
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ArchiveFormat(self, value):
        """
        Set the value of the ArchiveFormat input for this Choreo. ((required, string) Either tarball or zipball. Defaults to "tarball".)
        """
        InputSet._set_input(self, 'ArchiveFormat', value)
    def set_Ref(self, value):
        """
        Set the value of the Ref input for this Choreo. ((optional, string) A valid Git reference. Defaults to "master".)
        """
        InputSet._set_input(self, 'Ref', value)
    def set_Repo(self, value):
        """
        Set the value of the Repo input for this Choreo. ((required, string) The name of the repository.)
        """
        InputSet._set_input(self, 'Repo', value)
    def set_User(self, value):
        """
        Set the value of the User input for this Choreo. ((required, string) The GitHub username.)
        """
        InputSet._set_input(self, 'User', value)

class GetContentsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetContents Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from GitHub.)
        """
        return self._output.get('Response', None)

class GetContentsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetContentsResultSet(response, path)
