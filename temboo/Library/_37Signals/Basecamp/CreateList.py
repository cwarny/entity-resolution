# -*- coding: utf-8 -*-

###############################################################################
#
# CreateList
# Creates a new To-do list for a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CreateList')


    def new_input_set(self):
        return CreateListInputSet()

    def _make_result_set(self, result, path):
        return CreateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateListChoreographyExecution(session, exec_id, path)

class CreateListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Description(self, value):
        """
        Set the value of the Description input for this Choreo. ((optional, string) The description of the list to create.)
        """
        InputSet._set_input(self, 'Description', value)
    def set_MilestoneID(self, value):
        """
        Set the value of the MilestoneID input for this Choreo. ((optional, integer) The ID of an existing milestone to include with the new list.)
        """
        InputSet._set_input(self, 'MilestoneID', value)
    def set_Name(self, value):
        """
        Set the value of the Name input for this Choreo. ((optional, string) The name of the list to create.)
        """
        InputSet._set_input(self, 'Name', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project in which you're creating the new list.)
        """
        InputSet._set_input(self, 'ProjectID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class CreateListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No response is returned from Basecamp for update requests.)
        """
        return self._output.get('Response', None)

class CreateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateListResultSet(response, path)
