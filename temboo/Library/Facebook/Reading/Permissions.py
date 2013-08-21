# -*- coding: utf-8 -*-

###############################################################################
#
# Permissions
# Retrieves the set of permissions associated with a given access token.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Facebook.FacebookPermission import FacebookPermission

import json

class Permissions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Permissions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/Permissions')


    def new_input_set(self):
        return PermissionsInputSet()

    def _make_result_set(self, result, path):
        return PermissionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PermissionsChoreographyExecution(session, exec_id, path)

class PermissionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Permissions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ProfileID(self, value):
        """
        Set the value of the ProfileID input for this Choreo. ((optional, string) The id of the profile to access. Defaults to "me" indicating the authenticated user.)
        """
        InputSet._set_input(self, 'ProfileID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class PermissionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Permissions Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getPermissions(self):
        """
        Get a specific permission associated with the current access token
        """
        return [FacebookPermission(le) for le in self.getJSONFromString(self._output.get('Response', [])).get("data", [])]


class PermissionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PermissionsResultSet(response, path)
