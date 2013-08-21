# -*- coding: utf-8 -*-

###############################################################################
#
# ListByActivity
#  Returns all of the people in the specified collection for a particular activity.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListByActivity(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListByActivity Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Plus/People/ListByActivity')


    def new_input_set(self):
        return ListByActivityInputSet()

    def _make_result_set(self, result, path):
        return ListByActivityResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListByActivityChoreographyExecution(session, exec_id, path)

class ListByActivityInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListByActivity
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ActivityID(self, value):
        """
        Set the value of the ActivityID input for this Choreo. ((required, string) The ID of the activity to get the list of people for. ActiviyIDs can be retrieved by running the Google.Plus.Activities.Search Choreo.)
        """
        InputSet._set_input(self, 'ActivityID', value)
    def set_Callback(self, value):
        """
        Set the value of the Callback input for this Choreo. ((optional, string) Specifies a JavaScript function that will be passed the response data for using the API with JSONP.)
        """
        InputSet._set_input(self, 'Callback', value)
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
    def set_Collection(self, value):
        """
        Set the value of the Collection input for this Choreo. ((required, string) Valid values are: "plusoners" (lists all people who have +1'd this activity) and "resharers" (lists all people who have reshared this activity).)
        """
        InputSet._set_input(self, 'Collection', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See documentation for syntax rules.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of people to include in the response. Used for paging through results. Valid values are: 1 to 20. Default is 10.)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "NextPageToken" returned in the Choreo output. Used to page through large result sets.)
        """
        InputSet._set_input(self, 'PageToken', value)
    def set_PrettyPrint(self, value):
        """
        Set the value of the PrettyPrint input for this Choreo. ((optional, boolean) A flag used to pretty print the json response to make it more readable. Defaults to "true".)
        """
        InputSet._set_input(self, 'PrettyPrint', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        InputSet._set_input(self, 'RefreshToken', value)
    def set_UserIP(self, value):
        """
        Set the value of the UserIP input for this Choreo. ((optional, string) Identifies the IP address of the end user for whom the API call is being made. Used to enforce per-user quotas.)
        """
        InputSet._set_input(self, 'UserIP', value)

class ListByActivityResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListByActivity Choreo.
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

class ListByActivityChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListByActivityResultSet(response, path)
