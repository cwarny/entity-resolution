# -*- coding: utf-8 -*-

###############################################################################
#
# AddCollaboration
# Adds a collaboration for a single user to a specific folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddCollaboration(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddCollaboration Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Collaborations/AddCollaboration')


    def new_input_set(self):
        return AddCollaborationInputSet()

    def _make_result_set(self, result, path):
        return AddCollaborationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCollaborationChoreographyExecution(session, exec_id, path)

class AddCollaborationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddCollaboration
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
        Set the value of the FolderID input for this Choreo. ((required, string) The id of the folder that you want to create a collaboration for.)
        """
        InputSet._set_input(self, 'FolderID', value)
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((conditional, string) The email address of someone who this collaboration applies to. Required unless providing the UserID. Note, this does not need to be a Box user.)
        """
        InputSet._set_input(self, 'Login', value)
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((optional, string) The access level of the collaboration. Valid values are "viewer" or "editor". Defaults to "viewer".)
        """
        InputSet._set_input(self, 'Role', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The id of a Box user who this collaboration applies to. Required unless providing the EmailAddress.)
        """
        InputSet._set_input(self, 'UserID', value)


class AddCollaborationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddCollaboration Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class AddCollaborationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCollaborationResultSet(response, path)
