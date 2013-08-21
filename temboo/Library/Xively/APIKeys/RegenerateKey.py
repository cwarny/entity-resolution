# -*- coding: utf-8 -*-

###############################################################################
#
# RegenerateKey
# Allows you to regenerate a new key with the same attributes and permissions as a previous key.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RegenerateKey(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RegenerateKey Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Xively/APIKeys/RegenerateKey')


    def new_input_set(self):
        return RegenerateKeyInputSet()

    def _make_result_set(self, result, path):
        return RegenerateKeyResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RegenerateKeyChoreographyExecution(session, exec_id, path)

class RegenerateKeyInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RegenerateKey
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key you would like to regenerate. On successful regeneration, this API Key will no longer be valid.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_MasterAPIKey(self, value):
        """
        Set the value of the MasterAPIKey input for this Choreo. ((optional, string) Specify a MasterAPIKey with sufficient permissions if the APIKey you would like to regenerate does not have the permissions to do so.)
        """
        InputSet._set_input(self, 'MasterAPIKey', value)

class RegenerateKeyResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RegenerateKey Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_APIKeyLocation(self):
        """
        Retrieve the value for the "APIKeyLocation" output from this Choreo execution. ((string) The URL of the newly regenerated APIKey.)
        """
        return self._output.get('APIKeyLocation', None)
    def get_NewAPIKey(self):
        """
        Retrieve the value for the "NewAPIKey" output from this Choreo execution. ((string) The regenerated APIKey obtained from the APIKeyLocation returned by this Choreo.)
        """
        return self._output.get('NewAPIKey', None)

class RegenerateKeyChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RegenerateKeyResultSet(response, path)
