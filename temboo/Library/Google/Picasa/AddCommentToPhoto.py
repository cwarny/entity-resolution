# -*- coding: utf-8 -*-

###############################################################################
#
# AddCommentToPhoto
# Adds a comment to a specified photo in Google Picasa.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddCommentToPhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddCommentToPhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/AddCommentToPhoto')


    def new_input_set(self):
        return AddCommentToPhotoInputSet()

    def _make_result_set(self, result, path):
        return AddCommentToPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddCommentToPhotoChoreographyExecution(session, exec_id, path)

class AddCommentToPhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddCommentToPhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_AlbumID(self, value):
        """
        Set the value of the AlbumID input for this Choreo. ((required, integer) The id of the album which contains the photo you want to add a comment to.)
        """
        InputSet._set_input(self, 'AlbumID', value)
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
    def set_Comment(self, value):
        """
        Set the value of the Comment input for this Choreo. ((required, string) The comment that you want to add to a photo.)
        """
        InputSet._set_input(self, 'Comment', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo you want to add a comment to.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        InputSet._set_input(self, 'UserID', value)

class AddCommentToPhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddCommentToPhoto Choreo.
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

class AddCommentToPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddCommentToPhotoResultSet(response, path)
