# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateSettings
# Updates a user’s settings.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateSettings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateSettings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Settings/UpdateSettings')


    def new_input_set(self):
        return UpdateSettingsInputSet()

    def _make_result_set(self, result, path):
        return UpdateSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateSettingsChoreographyExecution(session, exec_id, path)

class UpdateSettingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateSettings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Settings(self, value):
        """
        Set the value of the Settings input for this Choreo. ((required, json) A JSON string containing the key/value pairs for the settings to update. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Settings', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class UpdateSettingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateSettings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class UpdateSettingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateSettingsResultSet(response, path)
