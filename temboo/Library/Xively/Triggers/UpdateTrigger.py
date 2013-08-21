# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateTrigger
# Updates an existing trigger.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateTrigger(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateTrigger Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Triggers/UpdateTrigger')


    def new_input_set(self):
        return UpdateTriggerInputSet()

    def _make_result_set(self, result, path):
        return UpdateTriggerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateTriggerChoreographyExecution(session, exec_id, path)

class UpdateTriggerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateTrigger
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ThresholdValue(self, value):
        """
        Set the value of the ThresholdValue input for this Choreo. ((optional, string) Threshold that will cause the trigger to activate. Include input only if changing Threshold Value.)
        """
        InputSet._set_input(self, 'ThresholdValue', value)
    def set_TriggerID(self, value):
        """
        Set the value of the TriggerID input for this Choreo. ((required, integer) TriggerID for the trigger that you wish to update.)
        """
        InputSet._set_input(self, 'TriggerID', value)
    def set_TriggerType(self, value):
        """
        Set the value of the TriggerType input for this Choreo. ((optional, string) Type of trigger. Include input only if changing TriggerType. Valid values: gt, gte, lt, lte, eq, change (any change), frozen (no updates for 15 minutes), or live (updated again after being frozen).)
        """
        InputSet._set_input(self, 'TriggerType', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((optional, string) The URL that the Xively trigger will post to when activated. Include input only if changing the URL. Ex: http://requestb.in)
        """
        InputSet._set_input(self, 'URL', value)

class UpdateTriggerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateTrigger Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful trigger update, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class UpdateTriggerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateTriggerResultSet(response, path)
