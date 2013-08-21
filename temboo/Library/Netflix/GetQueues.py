# -*- coding: utf-8 -*-

###############################################################################
#
# GetQueues
# Retrieves a list of a subscriber's queues.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetQueues(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetQueues Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Netflix/GetQueues')


    def new_input_set(self):
        return GetQueuesInputSet()

    def _make_result_set(self, result, path):
        return GetQueuesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetQueuesChoreographyExecution(session, exec_id, path)

class GetQueuesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetQueues
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Netflix (AKA the OAuth Consumer Key).)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_AccessTokenSecret(self, value):
        """
        Set the value of the AccessTokenSecret input for this Choreo. ((required, string) The Access Token Secret retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessTokenSecret', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) Set this to the maximum number of results to return. This number cannot be greater than 500. If you do not specify max_results, the default value is 25)
        """
        InputSet._set_input(self, 'MaxResults', value)
    def set_SharedSecret(self, value):
        """
        Set the value of the SharedSecret input for this Choreo. ((required, string) The Shared Secret provided by Netflix (AKA the OAuth Consumer Secret).)
        """
        InputSet._set_input(self, 'SharedSecret', value)
    def set_Sort(self, value):
        """
        Set the value of the Sort input for this Choreo. ((optional, string) Use this to specify the sort order for the queue entries. Sort order may be by queue_sequence, date_added, or alphabetical. The default sort order, if you do not specify one, is queue_sequence.)
        """
        InputSet._set_input(self, 'Sort', value)
    def set_StartIndex(self, value):
        """
        Set the value of the StartIndex input for this Choreo. ((optional, integer) The offset number of the results from the query.)
        """
        InputSet._set_input(self, 'StartIndex', value)
    def set_UpdatedMin(self, value):
        """
        Set the value of the UpdatedMin input for this Choreo. ((optional, date) If set, the response will include only those items with updated timestamps greater than or equal to the timestamp provided. Specify this value either in Unix time format (seconds since epoch).)
        """
        InputSet._set_input(self, 'UpdatedMin', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((required, string) The ID associated with the user whose queue information you want to retrieve.)
        """
        InputSet._set_input(self, 'UserID', value)

class GetQueuesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetQueues Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Netflix.)
        """
        return self._output.get('Response', None)

class GetQueuesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetQueuesResultSet(response, path)
