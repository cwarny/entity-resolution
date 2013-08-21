# -*- coding: utf-8 -*-

###############################################################################
#
# GetAllListItems
# Retrieves all items in a specified To-do list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAllListItems(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAllListItems Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/GetAllListItems')


    def new_input_set(self):
        return GetAllListItemsInputSet()

    def _make_result_set(self, result, path):
        return GetAllListItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAllListItemsChoreographyExecution(session, exec_id, path)

class GetAllListItemsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAllListItems
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_ListID(self, value):
        """
        Set the value of the ListID input for this Choreo. ((required, integer) The ID of the list for which you're returning items.)
        """
        InputSet._set_input(self, 'ListID', value)
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

class GetAllListItemsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAllListItems Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response returned from Basecamp.)
        """
        return self._output.get('Response', None)

class GetAllListItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAllListItemsResultSet(response, path)
