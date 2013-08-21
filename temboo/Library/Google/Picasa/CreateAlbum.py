# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAlbum
# Creates a photo album in a Google Picasa account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateAlbum(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAlbum Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/CreateAlbum')


    def new_input_set(self):
        return CreateAlbumInputSet()

    def _make_result_set(self, result, path):
        return CreateAlbumResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAlbumChoreographyExecution(session, exec_id, path)

class CreateAlbumInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAlbum
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
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
    def set_Keywords(self, value):
        """
        Set the value of the Keywords input for this Choreo. ((optional, string) Keywords to associate with the album you are creating separated by commas.)
        """
        InputSet._set_input(self, 'Keywords', value)
    def set_PhotoAccess(self, value):
        """
        Set the value of the PhotoAccess input for this Choreo. ((optional, string) The perssion level to specify for photo access. Defaults to 'public'.)
        """
        InputSet._set_input(self, 'PhotoAccess', value)
    def set_PhotoLocation(self, value):
        """
        Set the value of the PhotoLocation input for this Choreo. ((optional, string) The location to associate with the photo (i.e. Italy).)
        """
        InputSet._set_input(self, 'PhotoLocation', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_Summary(self, value):
        """
        Set the value of the Summary input for this Choreo. ((optional, string) The album summary.)
        """
        InputSet._set_input(self, 'Summary', value)
    def set_Timestamp(self, value):
        """
        Set the value of the Timestamp input for this Choreo. ((optional, date) The timestamp to associate with the photo.  Defaults to the current timestamp. Should be an epoch timestamp in milliseconds.)
        """
        InputSet._set_input(self, 'Timestamp', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the album.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        InputSet._set_input(self, 'UserID', value)

class CreateAlbumResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAlbum Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google Picasa.)
        """
        return self._output.get('Response', None)

class CreateAlbumChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAlbumResultSet(response, path)
