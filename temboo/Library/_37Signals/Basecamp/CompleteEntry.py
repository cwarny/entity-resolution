# -*- coding: utf-8 -*-

###############################################################################
#
# CompleteEntry
# Marks a specific calendar entry as completed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CompleteEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CompleteEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CompleteEntry')


    def new_input_set(self):
        return CompleteEntryInputSet()

    def _make_result_set(self, result, path):
        return CompleteEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CompleteEntryChoreographyExecution(session, exec_id, path)

class CompleteEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CompleteEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_EntryID(self, value):
        """
        Set the value of the EntryID input for this Choreo. ((required, integer) The ID for the calendar entry to mark as completed.)
        """
        InputSet._set_input(self, 'EntryID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project with the calendar entry to mark as completed.)
        """
        InputSet._set_input(self, 'ProjectID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class CompleteEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CompleteEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class CompleteEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CompleteEntryResultSet(response, path)
