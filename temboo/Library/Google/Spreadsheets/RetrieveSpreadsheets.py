# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveSpreadsheets
# Retrieves a list of spreadsheets that exist in your Google account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveSpreadsheets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveSpreadsheets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveSpreadsheets')


    def new_input_set(self):
        return RetrieveSpreadsheetsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveSpreadsheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveSpreadsheetsChoreographyExecution(session, exec_id, path)

class RetrieveSpreadsheetsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveSpreadsheets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google email address)
        """
        InputSet._set_input(self, 'Username', value)

class RetrieveSpreadsheetsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveSpreadsheets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class RetrieveSpreadsheetsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveSpreadsheetsResultSet(response, path)
