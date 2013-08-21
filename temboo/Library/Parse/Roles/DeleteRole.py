# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteRole
# Retrieves a given role.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteRole(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteRole Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Parse/Roles/DeleteRole')


    def new_input_set(self):
        return DeleteRoleInputSet()

    def _make_result_set(self, result, path):
        return DeleteRoleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteRoleChoreographyExecution(session, exec_id, path)

class DeleteRoleInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteRole
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, json) The ID of the role to retrieve.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_ApplicationID(self, value):
        """
        Set the value of the ApplicationID input for this Choreo. ((required, string) The Application ID provided by Parse.)
        """
        InputSet._set_input(self, 'ApplicationID', value)
    def set_RESTAPIKey(self, value):
        """
        Set the value of the RESTAPIKey input for this Choreo. ((required, string) The REST API Key provided by Parse.)
        """
        InputSet._set_input(self, 'RESTAPIKey', value)

class DeleteRoleResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteRole Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Parse.)
        """
        return self._output.get('Response', None)

class DeleteRoleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteRoleResultSet(response, path)
