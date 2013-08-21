# -*- coding: utf-8 -*-

###############################################################################
#
# AddWorksheet
# Creates a new worksheet within an existing spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddWorksheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddWorksheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/AddWorksheet')


    def new_input_set(self):
        return AddWorksheetInputSet()

    def _make_result_set(self, result, path):
        return AddWorksheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddWorksheetChoreographyExecution(session, exec_id, path)

class AddWorksheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddWorksheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_ColumnCount(self, value):
        """
        Set the value of the ColumnCount input for this Choreo. ((required, integer) The number of columns that you want to specify for the new worksheet)
        """
        InputSet._set_input(self, 'ColumnCount', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RowCount(self, value):
        """
        Set the value of the RowCount input for this Choreo. ((required, integer) The number of rows that you want to specify for the new worksheet)
        """
        InputSet._set_input(self, 'RowCount', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key associated with the spreadsheet that you want to add a worksheet to)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the new document to create)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google username)
        """
        InputSet._set_input(self, 'Username', value)

class AddWorksheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddWorksheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class AddWorksheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddWorksheetResultSet(response, path)
