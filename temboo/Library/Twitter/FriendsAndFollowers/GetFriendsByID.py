# -*- coding: utf-8 -*-

###############################################################################
#
# GetFriendsByID
# Retrieves a list of numeric IDs for every user the specified user is following (also known as their "friends").
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetFriendsByID(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetFriendsByID Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/GetFriendsByID')


    def new_input_set(self):
        return GetFriendsByIDInputSet()

    def _make_result_set(self, result, path):
        return GetFriendsByIDResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetFriendsByIDChoreographyExecution(session, exec_id, path)

class GetFriendsByIDInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetFriendsByID
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token provided by Twitter or retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ConsumerKey(self, value):
        """
        Set the value of the ConsumerKey input for this Choreo. ((required, string) The Consumer Key provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerKey', value)
    def set_ConsumerSecret(self, value):
        """
        Set the value of the ConsumerSecret input for this Choreo. ((required, string) The Consumer Secret provided by Twitter.)
        """
        InputSet._set_input(self, 'ConsumerSecret', value)
    def set_Cursor(self, value):
        """
        Set the value of the Cursor input for this Choreo. ((optional, string) Allows you to pass in the previous_cursor or next_cursor in order to page through results.)
        """
        InputSet._set_input(self, 'Cursor', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name of the user for whom to return results for. Required if UserId isn't specified.)
        """
        InputSet._set_input(self, 'ScreenName', value)
    def set_StringifyIDs(self, value):
        """
        Set the value of the StringifyIDs input for this Choreo. ((optional, boolean) A boolean flag indicating that Tweet IDs should be returned as strings.)
        """
        InputSet._set_input(self, 'StringifyIDs', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((conditional, integer) The ID of the user for whom to return results for. Required if ScreenName isn't specified.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetFriendsByIDResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetFriendsByID Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class GetFriendsByIDChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetFriendsByIDResultSet(response, path)
