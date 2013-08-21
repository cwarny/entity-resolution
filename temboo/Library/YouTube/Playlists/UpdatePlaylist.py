# -*- coding: utf-8 -*-

###############################################################################
#
# UpdatePlaylist
# Updates a playlist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleFileList import GoogleFileList

import json

class UpdatePlaylist(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdatePlaylist Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/Playlists/UpdatePlaylist')


    def new_input_set(self):
        return UpdatePlaylistInputSet()

    def _make_result_set(self, result, path):
        return UpdatePlaylistResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdatePlaylistChoreographyExecution(session, exec_id, path)

class UpdatePlaylistInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdatePlaylist
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The playlist's description.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields that are being set and that will be returned in the response (i.e. snippet,status).)
        """
        InputSet._set_input(self, 'Part', value)
    def set_PlaylistID(self, value):
        """
        Set the value of the PlaylistID input for this Choreo. ((required, string) The id of the playlist to update.)
        """
        InputSet._set_input(self, 'PlaylistID', value)
    def set_PrivacyStatus(self, value):
        """
        Set the value of the PrivacyStatus input for this Choreo. ((optional, string) The playlist's privacy status. Valid values are: private or public.)
        """
        InputSet._set_input(self, 'PrivacyStatus', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the playlist.)
        """
        InputSet._set_input(self, 'Title', value)

class UpdatePlaylistResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdatePlaylist Choreo.
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
    def getFileList(self):
        """
        Get a list of files
        """
        return GoogleFileList(self.getJSONFromString(self._output.get('Response', [])))

class UpdatePlaylistChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdatePlaylistResultSet(response, path)
