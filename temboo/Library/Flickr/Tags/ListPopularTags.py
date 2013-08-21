# -*- coding: utf-8 -*-

###############################################################################
#
# ListPopularTags
# Retrieves the popular tags for a given user (or the currently logged in user).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListPopularTags(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListPopularTags Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Flickr/Tags/ListPopularTags')


    def new_input_set(self):
        return ListPopularTagsInputSet()

    def _make_result_set(self, result, path):
        return ListPopularTagsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListPopularTagsChoreographyExecution(session, exec_id, path)

class ListPopularTagsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListPopularTags
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Flickr (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_APISecret(self, value):
        """
        Set the value of the APISecret input for this Choreo. ((conditional, string) The API Secret provided by Flickr (AKA the OAuth Consumer Secret). Required unless UserID is provided.)
        """
        InputSet._set_input(self, 'APISecret', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((conditional, string) The Access Token Secret retrieved during the OAuth process. Required unless UserID is provided.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((conditional, string) The Access Token retrieved during the OAuth process. Required unless UserID is provided.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Number of popular tags to return. defaults to 10 when this argument is not present.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: xml and json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, string) The NSID of the user to fetch the tag list for. Required unless providing all OAuth parameters. When OAuth parameters are passed, the authenticated user is assumed.)
        """
        InputSet._set_input(self, 'UserID', value)

class ListPopularTagsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListPopularTags Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Flickr.)
        """
        return self._output.get('Response', None)

class ListPopularTagsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListPopularTagsResultSet(response, path)
