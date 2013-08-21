# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateAccountObject
# Updates an Account Object name.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateAccountObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateAccountObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/UpdateAccountObject')


    def new_input_set(self):
        return UpdateAccountObjectInputSet()

    def _make_result_set(self, result, path):
        return UpdateAccountObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateAccountObjectChoreographyExecution(session, exec_id, path)

class UpdateAccountObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateAccountObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountId(self, value):
        """
        Set the value of the AccountId input for this Choreo. ((required, string) The ID for the account you want to update)
        """
        InputSet._set_input(self, 'AccountId', value)
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) A new name to update the Account with)
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

class UpdateAccountObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateAccountObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Salesforce)
        """
        return self._output.get('Response', None)

class UpdateAccountObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateAccountObjectResultSet(response, path)
