# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveQueuedPosts
# Retrieves a list of queued posts for a specified Tumblr blog.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveQueuedPosts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveQueuedPosts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/Post/RetrieveQueuedPosts')


    def new_input_set(self):
        return RetrieveQueuedPostsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveQueuedPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveQueuedPostsChoreographyExecution(session, exec_id, path)

class RetrieveQueuedPostsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveQueuedPosts
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
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        InputSet._set_input(self, 'BaseHostname', value)
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

class RetrieveQueuedPostsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveQueuedPosts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrieveQueuedPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveQueuedPostsResultSet(response, path)
