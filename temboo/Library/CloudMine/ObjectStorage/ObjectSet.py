# -*- coding: utf-8 -*-

###############################################################################
#
# ObjectSet
# Allows you to update or create key/value pairs.

#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ObjectSet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ObjectSet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/ObjectStorage/ObjectSet')


    def new_input_set(self):
        return ObjectSetInputSet()

    def _make_result_set(self, result, path):
        return ObjectSetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObjectSetChoreographyExecution(session, exec_id, path)

class ObjectSetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ObjectSet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Data(self, value):
        """
        Set the value of the Data input for this Choreo. ((required, json) A valid JSON object containing key/value pairs.)
        """
        InputSet._set_input(self, 'Data', value)
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        InputSet._set_input(self, 'SessionToken', value)

class ObjectSetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ObjectSet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class ObjectSetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObjectSetResultSet(response, path)
