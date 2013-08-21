# -*- coding: utf-8 -*-

###############################################################################
#
# CreateFriendship
# Allows you to follow another Twitter user by specifying a Twitter user id or screen name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateFriendship(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateFriendship Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/CreateFriendship')


    def new_input_set(self):
        return CreateFriendshipInputSet()

    def _make_result_set(self, result, path):
        return CreateFriendshipResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateFriendshipChoreographyExecution(session, exec_id, path)

class CreateFriendshipInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateFriendship
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
    def set_Follow(self, value):
        """
        Set the value of the Follow input for this Choreo. ((optional, boolean) A boolean flag that enables notifications for the target user when set to true.)
        """
        InputSet._set_input(self, 'Follow', value)
    def set_ScreenName(self, value):
        """
        Set the value of the ScreenName input for this Choreo. ((conditional, string) The screen name for the friend you want to create a friendship with. Required if UserId isn't specified.)
        """
        InputSet._set_input(self, 'ScreenName', value)
    def set_UserId(self, value):
        """
        Set the value of the UserId input for this Choreo. ((conditional, integer) The user id for the friend you want to create a friendship with. Required if ScreenName isn't specified.)
        """
        InputSet._set_input(self, 'UserId', value)

class CreateFriendshipResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateFriendship Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class CreateFriendshipChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateFriendshipResultSet(response, path)
