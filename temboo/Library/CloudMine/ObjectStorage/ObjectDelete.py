# -*- coding: utf-8 -*-

###############################################################################
#
# ObjectDelete
# Deletes one or more specified keys.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ObjectDelete(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ObjectDelete Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/CloudMine/ObjectStorage/ObjectDelete')


    def new_input_set(self):
        return ObjectDeleteInputSet()

    def _make_result_set(self, result, path):
        return ObjectDeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObjectDeleteChoreographyExecution(session, exec_id, path)

class ObjectDeleteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ObjectDelete
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_All(self, value):
        """
        Set the value of the All input for this Choreo. ((conditional, boolean) Indicates that all keys should be deleted if the Keys input is left empty. Set to "true" to delete all keys.)
        """
        InputSet._set_input(self, 'All', value)
    def set_ApplicationIdentifier(self, value):
        """
        Set the value of the ApplicationIdentifier input for this Choreo. ((required, string) The application identifier provided by CloudMine after registering your app.)
        """
        InputSet._set_input(self, 'ApplicationIdentifier', value)
    def set_Keys(self, value):
        """
        Set the value of the Keys input for this Choreo. ((conditional, string) A comma separated list of keys to delete. Required unless specifying "true" for the All parameter.)
        """
        InputSet._set_input(self, 'Keys', value)
    def set_SessionToken(self, value):
        """
        Set the value of the SessionToken input for this Choreo. ((conditional, string) The session token for an existing user (returned by the AccountLogin Choreo). This is only required if your app is performing this operation on behalf of another user.)
        """
        InputSet._set_input(self, 'SessionToken', value)

class ObjectDeleteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ObjectDelete Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from CloudMine.)
        """
        return self._output.get('Response', None)

class ObjectDeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObjectDeleteResultSet(response, path)
