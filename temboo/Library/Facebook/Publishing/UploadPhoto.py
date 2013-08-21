# -*- coding: utf-8 -*-

###############################################################################
#
# UploadPhoto
# Uploads a photo to a given album.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UploadPhoto(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UploadPhoto Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Publishing/UploadPhoto')


    def new_input_set(self):
        return UploadPhotoInputSet()

    def _make_result_set(self, result, path):
        return UploadPhotoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UploadPhotoChoreographyExecution(session, exec_id, path)

class UploadPhotoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UploadPhoto
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_AlbumID(self, value):
        """
        Set the value of the AlbumID input for this Choreo. ((required, string) The id of the album to upload the photo to.)
        """
        InputSet._set_input(self, 'AlbumID', value)
    def set_Message(self, value):
        """
        Set the value of the Message input for this Choreo. ((optional, string) A message to attach to the photo.)
        """
        InputSet._set_input(self, 'Message', value)
    def set_Photo(self, value):
        """
        Set the value of the Photo input for this Choreo. ((conditional, any) The image contents formatted as a Base64 encoded string.)
        """
        InputSet._set_input(self, 'Photo', value)
    def set_Place(self, value):
        """
        Set the value of the Place input for this Choreo. ((optional, string) A location associated with a Photo.)
        """
        InputSet._set_input(self, 'Place', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Source(self, value):
        """
        Set the value of the Source input for this Choreo. ((optional, string) A link to the source image of the photo.)
        """
        InputSet._set_input(self, 'Source', value)


class UploadPhotoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UploadPhoto Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)
    def getFacebookObjectId(self):
        """
        Get the ID of the object that has been created
        """
        return self.getJSONFromString(self._output.get('Response', [])).get("id", [])

class UploadPhotoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UploadPhotoResultSet(response, path)
