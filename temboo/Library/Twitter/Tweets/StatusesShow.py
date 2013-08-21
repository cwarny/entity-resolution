# -*- coding: utf-8 -*-

###############################################################################
#
# StatusesShow
# Retrieves a single Tweet with a given ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class StatusesShow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the StatusesShow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Tweets/StatusesShow')


    def new_input_set(self):
        return StatusesShowInputSet()

    def _make_result_set(self, result, path):
        return StatusesShowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusesShowChoreographyExecution(session, exec_id, path)

class StatusesShowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the StatusesShow
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
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The numerical ID of the desired Tweet..)
        """
        InputSet._set_input(self, 'ID', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) When set to true, the response will include the "entities" node.)
        """
        InputSet._set_input(self, 'IncludeEntities', value)
    def set_IncludeMyRetweet(self, value):
        """
        Set the value of the IncludeMyRetweet input for this Choreo. ((optional, boolean) When set to true, any Tweets returned that have been retweeted by the authenticating user will include an additional current_user_retweet node, containing the ID of the source status for the retweet.)
        """
        InputSet._set_input(self, 'IncludeMyRetweet', value)
    def set_TrimUser(self, value):
        """
        Set the value of the TrimUser input for this Choreo. ((optional, boolean) When set to true, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false.)
        """
        InputSet._set_input(self, 'TrimUser', value)

class StatusesShowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the StatusesShow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class StatusesShowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusesShowResultSet(response, path)
