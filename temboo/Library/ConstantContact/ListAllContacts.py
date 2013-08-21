# -*- coding: utf-8 -*-

###############################################################################
#
# ListAllContacts
# Retrieves a list of all contacts from Constant Contact.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListAllContacts(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListAllContacts Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/ListAllContacts')


    def new_input_set(self):
        return ListAllContactsInputSet()

    def _make_result_set(self, result, path):
        return ListAllContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllContactsChoreographyExecution(session, exec_id, path)

class ListAllContactsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListAllContacts
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Constant Contact.)
        """
        InputSet._set_input(self, 'APIKey', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Constant Contact password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_UserName(self, value):
        """
        Set the value of the UserName input for this Choreo. ((required, string) Your Constant Contact username.)
        """
        InputSet._set_input(self, 'UserName', value)

class ListAllContactsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListAllContacts Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Constant Contact.)
        """
        return self._output.get('Response', None)

class ListAllContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllContactsResultSet(response, path)
