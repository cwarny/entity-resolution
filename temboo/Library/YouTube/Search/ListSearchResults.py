# -*- coding: utf-8 -*-

###############################################################################
#
# ListSearchResults
# Returns a list of search results that match the specified query parameters.
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

class ListSearchResults(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListSearchResults Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/Search/ListSearchResults')


    def new_input_set(self):
        return ListSearchResultsInputSet()

    def _make_result_set(self, result, path):
        return ListSearchResultsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListSearchResultsChoreographyExecution(session, exec_id, path)

class ListSearchResultsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListSearchResults
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((optional, string) The API Key provided by Google for simple API access when you do not need to access user data.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ChannelID(self, value):
        """
        Set the value of the ChannelID input for this Choreo. ((optional, string) Indicates that the response should only contain resources created by this channel.)
        """
        InputSet._set_input(self, 'ChannelID', value)
    def set_ChannelType(self, value):
        """
        Set the value of the ChannelType input for this Choreo. ((optional, string) Restricts a search to a particular type of channel. Valid values are: "any" (returns all channels) and "show" (only retrieves shows).)
        """
        InputSet._set_input(self, 'ChannelType', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((optional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((optional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Indicates how the results are sorted. Valid values are: date, rating, relevance, and viewCount.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) Specifies a comma-separated list of one or more search resource properties that the API response will include. Part names that you can pass are 'id' and 'snippet' (the default).)
        """
        InputSet._set_input(self, 'Part', value)
    def set_PublishedAfter(self, value):
        """
        Set the value of the PublishedAfter input for this Choreo. ((optional, date) Returns only results created after the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        InputSet._set_input(self, 'PublishedAfter', value)
    def set_PublishedBefore(self, value):
        """
        Set the value of the PublishedBefore input for this Choreo. ((optional, date) Returns only results created before the specified time (formatted as a RFC 3339 date-time i.e. 1970-01-01T00:00:00Z).)
        """
        InputSet._set_input(self, 'PublishedBefore', value)
    def set_Query(self, value):
        """
        Set the value of the Query input for this Choreo. ((conditional, string) A query string for searching videos.)
        """
        InputSet._set_input(self, 'Query', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((optional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_RegionCode(self, value):
        """
        Set the value of the RegionCode input for this Choreo. ((optional, string) Returns results for the specified country. The parameter value is an ISO 3166-1 alpha-2 country code.)
        """
        InputSet._set_input(self, 'RegionCode', value)
    def set_RelatedToVideoID(self, value):
        """
        Set the value of the RelatedToVideoID input for this Choreo. ((optional, string) Retrieves a list of videos that are related to this video id. When using this parameter, the Type parameter must be set to video.)
        """
        InputSet._set_input(self, 'RelatedToVideoID', value)
    def set_TopicID(self, value):
        """
        Set the value of the TopicID input for this Choreo. ((optional, string) Returns only results associated with the specified topic.)
        """
        InputSet._set_input(self, 'TopicID', value)
    def set_Type(self, value):
        """
        Set the value of the Type input for this Choreo. ((optional, string) Restricts a search query to only retrieve a particular type of resource. The default value is: video,channel,playlist.)
        """
        InputSet._set_input(self, 'Type', value)
    def set_VideoCaption(self, value):
        """
        Set the value of the VideoCaption input for this Choreo. ((optional, string) Returns filtered results based on whether videos have captions. Valid values are: any (the default), closedCaption (only returns videos with captions), or none (only returns videos without captions).)
        """
        InputSet._set_input(self, 'VideoCaption', value)
    def set_VideoCategoryID(self, value):
        """
        Set the value of the VideoCategoryID input for this Choreo. ((optional, string) Filters video search results based on their category.)
        """
        InputSet._set_input(self, 'VideoCategoryID', value)
    def set_VideoDefinition(self, value):
        """
        Set the value of the VideoDefinition input for this Choreo. ((optional, string) Filters video results based high or standard definition. Valid values are: any, high, or standard.)
        """
        InputSet._set_input(self, 'VideoDefinition', value)
    def set_VideoDimension(self, value):
        """
        Set the value of the VideoDimension input for this Choreo. ((optional, string) Restrict a search to only retrieve 2D or 3D videos. Valid values are: 2d, 3d, or any.)
        """
        InputSet._set_input(self, 'VideoDimension', value)
    def set_VideoDuration(self, value):
        """
        Set the value of the VideoDuration input for this Choreo. ((optional, string) Filters search results based on the video duration. Valid values are: any, long, medium, and short.)
        """
        InputSet._set_input(self, 'VideoDuration', value)
    def set_VideoEmbeddable(self, value):
        """
        Set the value of the VideoEmbeddable input for this Choreo. ((optional, string) Filters search results to include only videos that can be embedded into a webpage. Valid values are: any (the default) or true (which will enable this filter).)
        """
        InputSet._set_input(self, 'VideoEmbeddable', value)
    def set_VideoLicense(self, value):
        """
        Set the value of the VideoLicense input for this Choreo. ((optional, string) Filters search results to only include videos with a particular license. Valid values are: any, creativeCommon, and youtube.)
        """
        InputSet._set_input(self, 'VideoLicense', value)
    def set_VideoSyndicated(self, value):
        """
        Set the value of the VideoSyndicated input for this Choreo. ((optional, string) Filters search results for videos that can be played outside of youtube.com. Valid values are: any (the default) or true (which will enable this filter).)
        """
        InputSet._set_input(self, 'VideoSyndicated', value)
    def set_VideoType(self, value):
        """
        Set the value of the VideoType input for this Choreo. ((optional, string) Filters search results to a particular type of videos. Valid values are: any, episode, and movie.)
        """
        InputSet._set_input(self, 'VideoType', value)

class ListSearchResultsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListSearchResults Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from YouTube.)
        """
        return self._output.get('Response', None)
    def getFileList(self):
        """
        Get a list of files
        """
        return GoogleFileList(self.getJSONFromString(self._output.get('Response', [])))

class ListSearchResultsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListSearchResultsResultSet(response, path)
