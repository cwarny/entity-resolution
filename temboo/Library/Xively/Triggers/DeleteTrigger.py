# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteTrigger
# Deletes the specified trigger.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteTrigger(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteTrigger Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/Triggers/DeleteTrigger')


    def new_input_set(self):
        return DeleteTriggerInputSet()

    def _make_result_set(self, result, path):
        return DeleteTriggerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteTriggerChoreographyExecution(session, exec_id, path)

class DeleteTriggerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteTrigger
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Xively.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_TriggerID(self, value):
        """
        Set the value of the TriggerID input for this Choreo. ((required, integer) TriggerID for the trigger that you wish to delete.)
        """
        InputSet._set_input(self, 'TriggerID', value)

class DeleteTriggerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteTrigger Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a successful trigger deletion, the code should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteTriggerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteTriggerResultSet(response, path)
