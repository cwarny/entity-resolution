# -*- coding: utf-8 -*-

###############################################################################
#
# CreateEntry
# Adds a body measurement entry to a user's feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/GeneralMeasurements/CreateEntry')


    def new_input_set(self):
        return CreateEntryInputSet()

    def _make_result_set(self, result, path):
        return CreateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEntryChoreographyExecution(session, exec_id, path)

class CreateEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Entry(self, value):
        """
        Set the value of the Entry input for this Choreo. ((required, json) A JSON string containing the key/value pairs for the body measurement entry to create. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Entry', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)

class CreateEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) Contains the string 'true" when a new entry is created successfully.)
        """
        return self._output.get('Response', None)
    def get_URI(self):
        """
        Retrieve the value for the "URI" output from this Choreo execution. ((string) The entry uri that was created.)
        """
        return self._output.get('URI', None)

class CreateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEntryResultSet(response, path)
