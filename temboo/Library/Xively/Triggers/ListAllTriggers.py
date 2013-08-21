# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllTriggers
# Returns all triggers for the authenticated account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllTriggers(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllTriggers Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Triggers/ListAllTriggers')


    def new_input_set(self):
        return ListAllTriggersInputSet()

    def _make_result_set(self, result, path):
        return ListAllTriggersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllTriggersChoreographyExecution(session, exec_id, path)

class ListAllTriggersInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllTriggers
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_FeedID(self, value):
        """
        Set the value of the FeedID input for this Choreo. ((optional, integer) Filter the returned triggers to only include those for the specified FeedID.)
        """
        InputSet._set_input(self, 'FeedID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ListAllTriggersResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllTriggers Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ListAllTriggersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllTriggersResultSet(response, path)
