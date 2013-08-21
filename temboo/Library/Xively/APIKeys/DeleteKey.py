# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteKey
# Deletes a specific API Key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/APIKeys/DeleteKey')


    def new_input_set(self):
        return DeleteKeyInputSet()

    def _make_result_set(self, result, path):
        return DeleteKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteKeyChoreographyExecution(session, exec_id, path)

class DeleteKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key you would like to delete.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_MasterAPIKey(self, value):
        """
        Set the value of the MasterAPIKey input for this Choreo. ((optional, string) Specify a MasterAPIKey with more permissions if the APIKey you would like to delete does not have sufficient permissions.)
        """
        InputSet._set_input(self, 'MasterAPIKey', value)

class DeleteKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code returned from Xively. For a valid deletion, the code returned should be 200.)
        """
        return self._output.get('ResponseStatusCode', None)

class DeleteKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteKeyResultSet(response, path)
