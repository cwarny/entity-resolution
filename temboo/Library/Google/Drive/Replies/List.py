# -*- coding: utf-8 -*-

###############################################################################
#
# List
# Lists all of the replies to a comment.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution
from temboo.outputs.Google.Drive.GoogleReplyList import GoogleReplyList

import json

class List(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the List Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Drive/Replies/List')


    def new_input_set(self):
        return ListInputSet()

    def _make_result_set(self, result, path):
        return ListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListChoreographyExecution(session, exec_id, path)

class ListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the List
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
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
    def set_CommentID(self, value):
        """
        Set the value of the CommentID input for this Choreo. ((required, string) The ID of the comment.)
        """
        InputSet._set_input(self, 'CommentID', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_FileID(self, value):
        """
        Set the value of the FileID input for this Choreo. ((required, string) The ID of the file.)
        """
        InputSet._set_input(self, 'FileID', value)
    def set_IncludeDeleted(self, value):
        """
        Set the value of the IncludeDeleted input for this Choreo. ((optional, boolean) If set, this will succeed when retrieving a deleted reply. (Default: false))
        """
        InputSet._set_input(self, 'IncludeDeleted', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of replies to include in the response, used for paging. Acceptable values are 0 to 100, inclusive. (Default: 20).)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The continuation token, used to page through large result sets. To get the next page of results, set this parameter to the value of "nextPageToken" from the previous response.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)

class ListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the List Choreo.
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
    def getReplyList(self):
        """
        Get a list of replies
        """
        return GoogleReplyList(self.getJSONFromString(self._output.get('Response', [])))

class ListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListResultSet(response, path)
