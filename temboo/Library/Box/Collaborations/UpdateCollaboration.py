# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateCollaboration
# Edits an existing collaboration.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateCollaboration(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateCollaboration Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Collaborations/UpdateCollaboration')


    def new_input_set(self):
        return UpdateCollaborationInputSet()

    def _make_result_set(self, result, path):
        return UpdateCollaborationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateCollaborationChoreographyExecution(session, exec_id, path)

class UpdateCollaborationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateCollaboration
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_CollaborationID(self, value):
        """
        Set the value of the CollaborationID input for this Choreo. ((required, string) The id of the collaboration to edit.)
        """
        InputSet._set_input(self, 'CollaborationID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma-separated list of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((conditional, string) The access level of the collaboration. Valid values are "viewer" or "editor". Defaults to "viewer". This value can only be updated by the owner of the folder.)
        """
        InputSet._set_input(self, 'Role', value)
    def set_Status(self, value):
        """
        Set the value of the Status input for this Choreo. ((conditional, string) Whether this collaboration has been accepted. Valid values are: "accepted" or "rejected". This value can only be updated by the user who has been invited to the collaboration.)
        """
        InputSet._set_input(self, 'Status', value)


class UpdateCollaborationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateCollaboration Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class UpdateCollaborationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateCollaborationResultSet(response, path)
