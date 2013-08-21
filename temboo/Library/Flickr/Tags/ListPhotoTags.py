# -*- coding: utf-8 -*-

###############################################################################
#
# ListPhotoTags
# Retrieves the tag list for a given photo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPhotoTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPhotoTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Tags/ListPhotoTags')


    def new_input_set(self):
        return ListPhotoTagsInputSet()

    def _make_result_set(self, result, path):
        return ListPhotoTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPhotoTagsChoreographyExecution(session, exec_id, path)

class ListPhotoTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPhotoTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((optional, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret). Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((optional, string) The Access Token Secret retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) The Access Token retrieved during the OAuth process. Required when accessing a protected resource.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_PhotoID(self, value):
        """
        Set the value of the PhotoID input for this Choreo. ((required, integer) The id of the photo to return tags for.)
        """
        InputSet._set_input(self, 'PhotoID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListPhotoTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPhotoTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPhotoTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPhotoTagsResultSet(response, path)
