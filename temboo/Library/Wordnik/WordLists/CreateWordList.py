# -*- coding: utf-8 -*-

###############################################################################
#
# CreateWordList
# Creates a new word list for the specified user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateWordList(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateWordList Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Wordnik/WordLists/CreateWordList')


    def new_input_set(self):
        return CreateWordListInputSet()

    def _make_result_set(self, result, path):
        return CreateWordListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateWordListChoreographyExecution(session, exec_id, path)

class CreateWordListInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateWordList
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key obtained from Wordnik.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_ListDescription(self, value):
        """
        Set the value of the ListDescription input for this Choreo. ((required, string) A description of the list to create.)
        """
        InputSet._set_input(self, 'ListDescription', value)
    def set_ListName(self, value):
        """
        Set the value of the ListName input for this Choreo. ((required, string) Name of list to create.)
        """
        InputSet._set_input(self, 'ListName', value)
    def set_ListStatus(self, value):
        """
        Set the value of the ListStatus input for this Choreo. ((optional, string) Determines whether the list to cretae is public or private. Acceptable values: PUBLIC or PRIVATE.)
        """
        InputSet._set_input(self, 'ListStatus', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, string) The Password of the Wordnik account.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The Username of the Wordnik account.)
        """
        InputSet._set_input(self, 'Username', value)

class CreateWordListResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateWordList Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Wordnik.)
        """
        return self._output.get('Response', None)

class CreateWordListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateWordListResultSet(response, path)
