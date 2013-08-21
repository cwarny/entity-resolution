# -*- coding: utf-8 -*-

###############################################################################
#
# DirectMessagesSent
# Retrieves the 20 most recent direct messages sent by the authenticating user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DirectMessagesSent(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DirectMessagesSent Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Twitter/DirectMessages/DirectMessagesSent')


    def new_input_set(self):
        return DirectMessagesSentInputSet()

    def _make_result_set(self, result, path):
        return DirectMessagesSentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DirectMessagesSentChoreographyExecution(session, exec_id, path)

class DirectMessagesSentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DirectMessagesSent
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
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Specifies the number of records to retrieve up to a maximum of 200.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_IncludeEntities(self, value):
        """
        Set the value of the IncludeEntities input for this Choreo. ((optional, boolean) When set to true, the response will include the "entities" node.)
        """
        InputSet._set_input(self, 'IncludeEntities', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, integer) Returns results with an ID less than (older than) or equal to the specified ID.)
        """
        InputSet._set_input(self, 'MaxID', value)
    def set_Page(self, value):
        """
        Set the value of the Page input for this Choreo. ((optional, integer) Specifies the page of results to retrieve.)
        """
        InputSet._set_input(self, 'Page', value)
    def set_SinceID(self, value):
        """
        Set the value of the SinceID input for this Choreo. ((optional, integer) Returns results with an ID greater than (more recent than) the specified ID.)
        """
        InputSet._set_input(self, 'SinceID', value)

class DirectMessagesSentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DirectMessagesSent Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Twitter.)
        """
        return self._output.get('Response', None)

class DirectMessagesSentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DirectMessagesSentResultSet(response, path)
