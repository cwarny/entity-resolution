# -*- coding: utf-8 -*-

###############################################################################
#
# ReadKey
# Returns a JSON or XML representation of the specified APIKey.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReadKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReadKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/APIKeys/ReadKey')


    def new_input_set(self):
        return ReadKeyInputSet()

    def _make_result_set(self, result, path):
        return ReadKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReadKeyChoreographyExecution(session, exec_id, path)

class ReadKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReadKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key you would like to return information on.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_MasterAPIKey(self, value):
        """
        Set the value of the MasterAPIKey input for this Choreo. ((optional, string) Specify a MasterAPIKey with more permissions if the APIKey you would like to view does not have sufficient (read) permissions.)
        """
        InputSet._set_input(self, 'MasterAPIKey', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "json" (the default) and "xml".)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ReadKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReadKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Xively.)
        """
        return self._output.get('Response', None)

class ReadKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReadKeyResultSet(response, path)
