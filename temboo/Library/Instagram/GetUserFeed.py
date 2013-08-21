# -*- coding: utf-8 -*-

###############################################################################
#
# GetUserFeed
# Retrieves the authenticated user's feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUserFeed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUserFeed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Instagram/GetUserFeed')


    def new_input_set(self):
        return GetUserFeedInputSet()

    def _make_result_set(self, result, path):
        return GetUserFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUserFeedChoreographyExecution(session, exec_id, path)

class GetUserFeedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUserFeed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved during the OAuth 2.0 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Count(self, value):
        """
        Set the value of the Count input for this Choreo. ((optional, integer) Count of media to return.)
        """
        InputSet._set_input(self, 'Count', value)
    def set_MaxID(self, value):
        """
        Set the value of the MaxID input for this Choreo. ((optional, integer) Returns media earlier than this max_id.)
        """
        InputSet._set_input(self, 'MaxID', value)
    def set_MinID(self, value):
        """
        Set the value of the MinID input for this Choreo. ((optional, integer) Returns media later than this min_id.)
        """
        InputSet._set_input(self, 'MinID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the user that you want to retrieve. Defaults to 'self' which will return the user associated with the access token.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetUserFeedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUserFeed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Instagram.)
        """
        return self._output.get('Response', None)

class GetUserFeedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetUserFeedResultSet(response, path)
