# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteEntry
# Removes an individual nutrition entry from a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/Nutrition/DeleteEntry')


    def new_input_set(self):
        return DeleteEntryInputSet()

    def _make_result_set(self, result, path):
        return DeleteEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteEntryChoreographyExecution(session, exec_id, path)

class DeleteEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, string) This can be the individual id of the nutrition entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /nutrition/-12985593-1350864000000).)
        """
        InputSet._set_input(self, 'EntryID', value)

class DeleteEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((boolean) Contains the string "true" when an entry is deleted successfully.)
        """
        return self._output.get('Response', None)

class DeleteEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteEntryResultSet(response, path)
