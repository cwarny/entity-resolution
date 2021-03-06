# -*- coding: utf-8 -*-

###############################################################################
#
# HomeTimeline
# Retrieves a collection of the most recent Tweets and retweets posted by the authenticating user and the users they follow.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HomeTimeline(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HomeTimeline Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/Timelines/HomeTimeline')


    def new_input_set(self):
        return HomeTimelineInputSet()

    def _make_result_set(self, result, path):
        return HomeTimelineResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HomeTimelineChoreographyExecution(session, exec_id, path)

class HomeTimelineInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HomeTimeline
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
    def set_ContributorDetails(self, value):
        """
        Set the value of the ContributorDetails input for this Choreo. ((optional, boolean) Set to true to include the screen_name of the contributor. By default only the user_id of the contributor is included.)
        """
        InputSet._set_input(self, 'ContributorDetails', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of records to retrieve. Must be less than or equal to 200. Defaults to 20.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_ExcludeReplies(self, value):
        """
        Set the value of the ExcludeReplies input for this Choreo. ((optional, boolean) Set to true to prevent replies from appearing in the returned timeline.)
        """
        InputSet._set_input(self, 'ExcludeReplies', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) When set to true, the response will include the "entities" node.)
        """
        InputSet._set_input(self, 'IncludeEntities', value)
    def set_MaxId(self, value):
        """
        Set the value of the MaxId input for this Choreo. ((optional, integer) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        InputSet._set_input(self, 'MaxId', value)
    def set_SinceId(self, value):
        """
        Set the value of the SinceId input for this Choreo. ((optional, integer) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        InputSet._set_input(self, 'SinceId', value)
    def set_TrimUser(self, value):
        """
        Set the value of the TrimUser input for this Choreo. ((optional, boolean) When set to true, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Defaults to false.)
        """
        InputSet._set_input(self, 'TrimUser', value)

class HomeTimelineResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HomeTimeline Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class HomeTimelineChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HomeTimelineResultSet(response, path)
