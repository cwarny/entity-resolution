# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateEntry
# Updates a sleep entry in a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Sleep/UpdateEntry')


    def new_input_set(self):
        return UpdateEntryInputSet()

    def _make_result_set(self, result, path):
        return UpdateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateEntryChoreographyExecution(session, exec_id, path)

class UpdateEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Entry(self, value):
        """
        Set the value of the Entry input for this Choreo. ((required, json) A JSON string containing the key/value pairs for the fields to be updated in the sleep entry. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Entry', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, string) This can be the individual id of the sleep entry, or you can pass the full uri for the entry as returned from the RetrieveEntries response (i.e. /sleep/-12985593-1347998400000).)
        """
        InputSet._set_input(self, 'EntryID', value)

class UpdateEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class UpdateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateEntryResultSet(response, path)
