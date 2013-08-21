# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteCollaboration
# Deletes a single collaboration.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteCollaboration(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteCollaboration Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Box/Collaborations/DeleteCollaboration')


    def new_input_set(self):
        return DeleteCollaborationInputSet()

    def _make_result_set(self, result, path):
        return DeleteCollaborationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteCollaborationChoreographyExecution(session, exec_id, path)

class DeleteCollaborationInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteCollaboration
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_CollaborationID(self, value):
        """
        Set the value of the CollaborationID input for this Choreo. ((required, string) The id of the collaboration to remove from a folder.)
        """
        InputSet._set_input(self, 'CollaborationID', value)


class DeleteCollaborationResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteCollaboration Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Box.)
        """
        return self._output.get('Response', None)

class DeleteCollaborationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteCollaborationResultSet(response, path)
