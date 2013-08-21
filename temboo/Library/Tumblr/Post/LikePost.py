# -*- coding: utf-8 -*-

###############################################################################
#
# LikePost
# Allows a user to like a specified post.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class LikePost(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the LikePost Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/Post/LikePost')


    def new_input_set(self):
        return LikePostInputSet()

    def _make_result_set(self, result, path):
        return LikePostResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LikePostChoreographyExecution(session, exec_id, path)

class LikePostInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the LikePost
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, integer) The ID of the post you want to like.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_ReblogKey(self, value):
        """
        Set the value of the ReblogKey input for this Choreo. ((required, string) The reblog key for the post id. This can be retrieved with the RetrievePublishedPosts Choreo.)
        """
        InputSet._set_input(self, 'ReblogKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_SecretKey(self, value):
        """
        Set the value of the SecretKey input for this Choreo. ((required, string) The Secret Key provided by Tumblr (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SecretKey', value)

class LikePostResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the LikePost Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class LikePostChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LikePostResultSet(response, path)
