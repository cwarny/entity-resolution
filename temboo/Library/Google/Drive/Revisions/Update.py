# -*- coding: utf-8 -*-

###############################################################################
#
# Update
# Updates a revision.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleRevision import GoogleRevision

import json

class Update(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Update Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Revisions/Update')


    def new_input_set(self):
        return UpdateInputSet()

    def _make_result_set(self, result, path):
        return UpdateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateChoreographyExecution(session, exec_id, path)

class UpdateInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Update
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestBody(self, value):
        """
        Set the value of the RequestBody input for this Choreo. ((required, json) A JSON representation of fields in a reply resource which shoud contain at least one key for pinned, publishAuto, published, or publishedOutsideDomain. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'RequestBody', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The ID of the file.)
        """
        InputSet._set_input(self, 'FileID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_RevisionID(self, value):
        """
        Set the value of the RevisionID input for this Choreo. ((required, string) The ID of the revision.)
        """
        InputSet._set_input(self, 'RevisionID', value)

class UpdateResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Update Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def getRevision(self):
        """
        A Google Drive revision resource
        """
        return GoogleRevision(self.getJSONFromString(self._output.get('Response', [])))

class UpdateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateResultSet(response, path)
