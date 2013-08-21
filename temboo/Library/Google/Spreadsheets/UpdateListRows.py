# -*- coding: utf-8 -*-

###############################################################################
#
# UpdateListRows
# Updates a worksheet row in a Google spreadsheet using a simple XML file you provide.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class UpdateListRows(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the UpdateListRows Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/UpdateListRows')


    def new_input_set(self):
        return UpdateListRowsInputSet()

    def _make_result_set(self, result, path):
        return UpdateListRowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateListRowsChoreographyExecution(session, exec_id, path)

class UpdateListRowsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the UpdateListRows
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RowsetXML(self, value):
        """
        Set the value of the RowsetXML input for this Choreo. ((required, xml) The row of data that you want to update in XML format. Your XML needs to be in the rowset/row schema described in the Choreo documentation.)
        """
        InputSet._set_input(self, 'RowsetXML', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RowId(self, value):
        """
        Set the value of the RowId input for this Choreo. ((required, string) The unique id of the row you want to update)
        """
        InputSet._set_input(self, 'RowId', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet that contains the worksheet you want to update)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google username)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique id of the worksheet that you want to update)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class UpdateListRowsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the UpdateListRows Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class UpdateListRowsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateListRowsResultSet(response, path)
