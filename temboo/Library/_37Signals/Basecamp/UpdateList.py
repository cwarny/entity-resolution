# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateList
# Updates a specified To-do list record 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/UpdateList')


    def new_input_set(self):
        return UpdateListInputSet()

    def _make_result_set(self, result, path):
        return UpdateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListChoreographyExecution(session, exec_id, path)

class UpdateListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The new description for the list.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, integer) The ID for the list to update.)
        """
        InputSet._set_input(self, 'ListID', value)
    def set_MilestoneID(self, value):
        """
        Set the value of the MilestoneID input for this Choreo. ((optional, integer) The ID of an existing milestone to add to the To-Do list.)
        """
        InputSet._set_input(self, 'MilestoneID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The new name for the list.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class UpdateListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No response is returned from Basecamp for update requests.)
        """
        return self._output.get('Response', None)

class UpdateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListResultSet(response, path)
