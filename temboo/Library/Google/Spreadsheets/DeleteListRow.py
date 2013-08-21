# -*- coding: utf-8 -*-

###############################################################################
#
# DeleteListRow
# Deletes a specified worksheet row from a Google spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DeleteListRow(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DeleteListRow Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/DeleteListRow')


    def new_input_set(self):
        return DeleteListRowInputSet()

    def _make_result_set(self, result, path):
        return DeleteListRowResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteListRowChoreographyExecution(session, exec_id, path)

class DeleteListRowInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the DeleteListRow
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EditLink(self, value):
        """
        Set the value of the EditLink input for this Choreo. ((conditional, string) The entry's edit link URL. Can be retrieved by running RetrieveListFeed and parsing the 'edit' link returned. When the edit link is provided, SpreadsheetKey, WorksheetId, and RowId are not needed.)
        """
        InputSet._set_input(self, 'EditLink', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RowId(self, value):
        """
        Set the value of the RowId input for this Choreo. ((conditional, string) The unique id of the row you want to delete. Required unless providing the EditLink.)
        """
        InputSet._set_input(self, 'RowId', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((conditional, string) The unique key of the spreadsheet associated with the row you want to delete. Required unless providing the EditLink.)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google username.)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((conditional, string) The unique id of the worksheet associated with the row you want to delete. Required unless providing the EditLink.)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class DeleteListRowResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the DeleteListRow Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class DeleteListRowChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteListRowResultSet(response, path)
