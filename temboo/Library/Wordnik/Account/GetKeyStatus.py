# -*- coding: utf-8 -*-

###############################################################################
#
# GetKeyStatus
# Obtains the status of the user's current API Key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetKeyStatus(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetKeyStatus Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/Account/GetKeyStatus')


    def new_input_set(self):
        return GetKeyStatusInputSet()

    def _make_result_set(self, result, path):
        return GetKeyStatusResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetKeyStatusChoreographyExecution(session, exec_id, path)

class GetKeyStatusInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetKeyStatus
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ResponseType(self, value):
        """
        Set the value of the ResponseType input for this Choreo. ((optional, string) Response can be either JSON or XML. Defaults to JSON.)
        """
        InputSet._set_input(self, 'ResponseType', value)

class GetKeyStatusResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetKeyStatus Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class GetKeyStatusChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetKeyStatusResultSet(response, path)
