# -*- coding: utf-8 -*-

###############################################################################
#
# RetrievePublishedPosts
# Retrieves published posts using various search and filter parameters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrievePublishedPosts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrievePublishedPosts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Tumblr/Post/RetrievePublishedPosts')


    def new_input_set(self):
        return RetrievePublishedPostsInputSet()

    def _make_result_set(self, result, path):
        return RetrievePublishedPostsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrievePublishedPostsChoreographyExecution(session, exec_id, path)

class RetrievePublishedPostsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrievePublishedPosts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Tumblr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_BaseHostname(self, value):
        """
        Set the value of the BaseHostname input for this Choreo. ((required, string) The standard or custom blog hostname (i.e. temboo.tumblr.com).)
        """
        InputSet._set_input(self, 'BaseHostname', value)
    def set_Format(self, value):
        """
        Set the value of the Format input for this Choreo. ((optional, string) Specifies the post format to return. Valid values are: text (Plain text, no HTML), raw (As entered by user). HTML is returned when left null.)
        """
        InputSet._set_input(self, 'Format', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((optional, integer) The specified post ID in order to return a single post.)
        """
        InputSet._set_input(self, 'ID', value)
    def set_Limit(self, value):
        """
        Set the value of the Limit input for this Choreo. ((optional, integer) The number of posts to return: 1- 20. Defaults to 20.)
        """
        InputSet._set_input(self, 'Limit', value)
    def set_NotesInfo(self, value):
        """
        Set the value of the NotesInfo input for this Choreo. ((optional, boolean) Indicates whether to return notes information (specify true or false). Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'NotesInfo', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((optional, integer) The post number to start at. Defaults to 0.)
        """
        InputSet._set_input(self, 'Offset', value)
    def set_ReblogInfo(self, value):
        """
        Set the value of the ReblogInfo input for this Choreo. ((optional, boolean) Indicates whether to return reblog information (specify 1 or 0). Defaults to 0 (false).)
        """
        InputSet._set_input(self, 'ReblogInfo', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Tag(self, value):
        """
        Set the value of the Tag input for this Choreo. ((optional, string) Limits the response to posts with the specified tag.)
        """
        InputSet._set_input(self, 'Tag', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) The type of post to return. Specify one of the following:  text, quote, link, answer, video, audio, photo. When null, all types are returned.)
        """
        InputSet._set_input(self, 'Type', value)

class RetrievePublishedPostsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrievePublishedPosts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Tumblr. Default is JSON, can be set to XML by entering 'xml' in ResponseFormat.)
        """
        return self._output.get('Response', None)

class RetrievePublishedPostsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrievePublishedPostsResultSet(response, path)
