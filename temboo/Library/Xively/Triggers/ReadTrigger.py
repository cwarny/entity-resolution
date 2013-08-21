# -*- coding: utf-8 -*-

###############################################################################
#
# ReadTrigger
# Returns a specific trigger for the authenticated account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReadTrigger(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadTrigger Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Triggers/ReadTrigger')


    def new_input_set(self):
        return ReadTriggerInputSet()

    def _make_result_set(self, result, path):
        return ReadTriggerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadTriggerChoreographyExecution(session, exec_id, path)

class ReadTriggerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadTrigger
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_TriggerID(self, value):
        """
        Set the value of the TriggerID input for this Choreo. ((required, integer) ID for the trigger that you wish to retrieve information about.)
        """
        InputSet._set_input(self, 'TriggerID', value)

class ReadTriggerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadTrigger Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ReadTriggerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReadTriggerResultSet(response, path)
