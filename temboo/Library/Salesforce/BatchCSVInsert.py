# -*- coding: utf-8 -*-

###############################################################################
#
# BatchCSVInsert
# Create Salesforce Objects of any type (Account, Lead, Contact, etc) by specifying rows in CSV format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class BatchCSVInsert(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the BatchCSVInsert Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/BatchCSVInsert')


    def new_input_set(self):
        return BatchCSVInsertInputSet()

    def _make_result_set(self, result, path):
        return BatchCSVInsertResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchCSVInsertChoreographyExecution(session, exec_id, path)

class BatchCSVInsertInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the BatchCSVInsert
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSVInput(self, value):
        """
        Set the value of the CSVInput input for this Choreo. ((conditional, multiline) CSV data to insert. Column names must match Salesforce field names exactly. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        InputSet._set_input(self, 'CSVInput', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Salesforce password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SalesforceObjectType(self, value):
        """
        Set the value of the SalesforceObjectType input for this Choreo. ((optional, string) The object type that you are inserting (i.e.Lead, Contact, Account). Defaults to Lead.)
        """
        InputSet._set_input(self, 'SalesforceObjectType', value)
    def set_SecurityToken(self, value):
        """
        Set the value of the SecurityToken input for this Choreo. ((required, string) Your Salesforce security token for making API calls.)
        """
        InputSet._set_input(self, 'SecurityToken', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Salesforce username.)
        """
        InputSet._set_input(self, 'Username', value)


class BatchCSVInsertResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the BatchCSVInsert Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Salesforce)
        """
        return self._output.get('Response', None)

class BatchCSVInsertChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BatchCSVInsertResultSet(response, path)
