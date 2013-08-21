# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateRole
# Updates an existing role.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateRole(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateRole Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Roles/UpdateRole')


    def new_input_set(self):
        return UpdateRoleInputSet()

    def _make_result_set(self, result, path):
        return UpdateRoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateRoleChoreographyExecution(session, exec_id, path)

class UpdateRoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateRole
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Role(self, value):
        """
        Set the value of the Role input for this Choreo. ((required, json) A JSON string containing the role information to be updated. See documentation for formatting details.)
        """
        InputSet._set_input(self, 'Role', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The ID of the role to update.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)

class UpdateRoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateRole Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class UpdateRoleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateRoleResultSet(response, path)
