# -*- coding: utf-8 -*-

###############################################################################
#
# ListMySubscriptions
# Returns a list of the authenticated user's subscriptions.
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

class ListMySubscriptions(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListMySubscriptions Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/YouTube/Subscriptions/ListMySubscriptions')


    def new_input_set(self):
        return ListMySubscriptionsInputSet()

    def _make_result_set(self, result, path):
        return ListMySubscriptionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMySubscriptionsChoreographyExecution(session, exec_id, path)

class ListMySubscriptionsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListMySubscriptions
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required for OAuth authentication unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Allows you to specify a subset of fields to include in the response using an xpath-like syntax (i.e. items/snippet/title).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_ForChannelId(self, value):
        """
        Set the value of the ForChannelId input for this Choreo. ((optional, string) A comma-separated list of channel IDs. The response will include only subscription matching these channels.)
        """
        InputSet._set_input(self, 'ForChannelId', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_Order(self, value):
        """
        Set the value of the Order input for this Choreo. ((optional, string) Indicates how the results are sorted. Valid values are: alphabetical, relevance, or unread.)
        """
        InputSet._set_input(self, 'Order', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((optional, string) A comma-separated list of fields to include. Valid values are: id, snippet, and contentDetails.)
        """
        InputSet._set_input(self, 'Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required for OAuth authentication unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class ListMySubscriptionsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListMySubscriptions Choreo.
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
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def getFileList(self):
        """
        Get a list of files
        """
        return GoogleFileList(self.getJSONFromString(self._output.get('Response', [])))

class ListMySubscriptionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMySubscriptionsResultSet(response, path)
