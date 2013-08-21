# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveSettings
# Retrieves a user’s settings including a user's sharing and display preferences.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveSettings(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveSettings Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Settings/RetrieveSettings')


    def new_input_set(self):
        return RetrieveSettingsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSettingsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSettingsChoreographyExecution(session, exec_id, path)

class RetrieveSettingsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveSettings
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class RetrieveSettingsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveSettings Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveSettingsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveSettingsResultSet(response, path)
