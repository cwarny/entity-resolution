# -*- coding: utf-8 -*-

###############################################################################
#
# CreateAccountObject
# Creates new account object.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateAccountObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateAccountObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/CreateAccountObject')


    def new_input_set(self):
        return CreateAccountObjectInputSet()

    def _make_result_set(self, result, path):
        return CreateAccountObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateAccountObjectChoreographyExecution(session, exec_id, path)

class CreateAccountObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateAccountObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The name of the account to create)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Salesforce password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SecurityToken(self, value):
        """
        Set the value of the SecurityToken input for this Choreo. ((required, string) Your Salesforce security token used for making API calls.)
        """
        InputSet._set_input(self, 'SecurityToken', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Salesforce username.)
        """
        InputSet._set_input(self, 'Username', value)

class CreateAccountObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateAccountObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The full response from Salesforce)
        """
        return self._output.get('Response', None)

class CreateAccountObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateAccountObjectResultSet(response, path)
