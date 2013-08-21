# -*- coding: utf-8 -*-

###############################################################################
#
# ReorderLists
# Allows you to reorder To-do lists in a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ReorderLists(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ReorderLists Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/ReorderLists')


    def new_input_set(self):
        return ReorderListsInputSet()

    def _make_result_set(self, result, path):
        return ReorderListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ReorderListsChoreographyExecution(session, exec_id, path)

class ReorderListsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ReorderLists
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_FirstListID(self, value):
        """
        Set the value of the FirstListID input for this Choreo. ((required, integer) The ID number for the project's first To-Do list.)
        """
        InputSet._set_input(self, 'FirstListID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProjectID(self, value):
        """
        Set the value of the ProjectID input for this Choreo. ((required, integer) The ID for the project associated with the to-do lists that you are reordering.)
        """
        InputSet._set_input(self, 'ProjectID', value)
    def set_SecondListID(self, value):
        """
        Set the value of the SecondListID input for this Choreo. ((optional, integer) The ID number for the project's second To-Do list.)
        """
        InputSet._set_input(self, 'SecondListID', value)
    def set_ThirdListID(self, value):
        """
        Set the value of the ThirdListID input for this Choreo. ((optional, integer) The ID number for the project's third To-Do list.)
        """
        InputSet._set_input(self, 'ThirdListID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A Basecamp account username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class ReorderListsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ReorderLists Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (No response is returned from Basecamp for update requests.)
        """
        return self._output.get('Response', None)

class ReorderListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ReorderListsResultSet(response, path)
