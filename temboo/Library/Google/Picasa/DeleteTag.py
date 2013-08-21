# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTag
# Removes a tag from a specified photo in Google Picasa.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteTag(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteTag Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Picasa/DeleteTag')


    def new_input_set(self):
        return DeleteTagInputSet()

    def _make_result_set(self, result, path):
        return DeleteTagResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTagChoreographyExecution(session, exec_id, path)

class DeleteTagInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteTag
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_AlbumId(self, value):
        """
        Set the value of the AlbumId input for this Choreo. ((required, integer) The id for the album which has the tagged photo. Note that this can be retrieved by running the ListAlbums Choreo.)
        """
        InputSet._set_input(self, 'AlbumId', value)
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
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id for the photo that has a tag to delete.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_TagID(self, value):
        """
        Set the value of the TagID input for this Choreo. ((required, string) The Id (or tag name) for the tag that you want to delete.)
        """
        InputSet._set_input(self, 'TagID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) Google Picasa username. Defaults to 'default' which means the server will use the UserID of the user whose access token was specified.)
        """
        InputSet._set_input(self, 'UserID', value)

class DeleteTagResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteTag Choreo.
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

class DeleteTagChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTagResultSet(response, path)
