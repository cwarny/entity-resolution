# -*- coding: utf-8 -*-

###############################################################################
#
# FriendshipsShow
# Returns detailed information about the relationship between two users.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FriendshipsShow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FriendshipsShow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/FriendsAndFollowers/FriendshipsShow')


    def new_input_set(self):
        return FriendshipsShowInputSet()

    def _make_result_set(self, result, path):
        return FriendshipsShowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FriendshipsShowChoreographyExecution(session, exec_id, path)

class FriendshipsShowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FriendshipsShow
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
    def set_SourceScreenName(self, value):
        """
        Set the value of the SourceScreenName input for this Choreo. ((conditional, string) The screen_name of the subject user. Required unless specifying the SourceUserID instead.)
        """
        InputSet._set_input(self, 'SourceScreenName', value)
    def set_SourceUserID(self, value):
        """
        Set the value of the SourceUserID input for this Choreo. ((conditional, integer) The ID of the subject user. Required unless specifying the SourceScreenName instead.)
        """
        InputSet._set_input(self, 'SourceUserID', value)
    def set_TargetScreenName(self, value):
        """
        Set the value of the TargetScreenName input for this Choreo. ((conditional, string) The screen_name of the target user. Required unless specifying the TargetUserID instead.)
        """
        InputSet._set_input(self, 'TargetScreenName', value)
    def set_TargetUserID(self, value):
        """
        Set the value of the TargetUserID input for this Choreo. ((conditional, integer) The ID of the target user. Required unless specifying the TargetScreenName instead.)
        """
        InputSet._set_input(self, 'TargetUserID', value)

class FriendshipsShowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FriendshipsShow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class FriendshipsShowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FriendshipsShowResultSet(response, path)
