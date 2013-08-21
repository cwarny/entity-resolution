# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteWorksheet
# Deletes a specified worksheet from an existing spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteWorksheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteWorksheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/DeleteWorksheet')


    def new_input_set(self):
        return DeleteWorksheetInputSet()

    def _make_result_set(self, result, path):
        return DeleteWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteWorksheetChoreographyExecution(session, exec_id, path)

class DeleteWorksheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteWorksheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key associated with the spreadsheet that contains a worksheet you want to delete)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google username)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique id associated with the worksheet that you want to delete)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class DeleteWorksheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteWorksheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class DeleteWorksheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteWorksheetResultSet(response, path)
