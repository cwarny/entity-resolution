# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveEntry
# Retrieves a body measurement entry from a user’s feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RunKeeper/GeneralMeasurements/RetrieveEntry')


    def new_input_set(self):
        return RetrieveEntryInputSet()

    def _make_result_set(self, result, path):
        return RetrieveEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveEntryChoreographyExecution(session, exec_id, path)

class RetrieveEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved after the final step in the OAuth2 process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, string) This can be the individual id of the body measurement entry, or you can pass the full uri for the entry as returned from the RetrieveEntries Choreo (i.e. /generalMeasurements/24220709).)
        """
        InputSet._set_input(self, 'EntryID', value)

class RetrieveEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from RunKeeper.)
        """
        return self._output.get('Response', None)

class RetrieveEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveEntryResultSet(response, path)
