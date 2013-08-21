# -*- coding: utf-8 -*-

###############################################################################
#
# AddListRows
# Adds one or more rows to a worksheet in a Google spreadsheet using a simple XML file you provide.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class AddListRows(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the AddListRows Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/AddListRows')


    def new_input_set(self):
        return AddListRowsInputSet()

    def _make_result_set(self, result, path):
        return AddListRowsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddListRowsChoreographyExecution(session, exec_id, path)

class AddListRowsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the AddListRows
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RowsetXML(self, value):
        """
        Set the value of the RowsetXML input for this Choreo. ((required, xml) The rows of data that you want to add to a worksheet in XML format. Your XML needs to be in the rowset/row schema described in the Choreo documentation.)
        """
        InputSet._set_input(self, 'RowsetXML', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique key of the spreadsheet that contains the worksheet you want to add rows to)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google username)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique id of the worksheet that you want to add rows to)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class AddListRowsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the AddListRows Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class AddListRowsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddListRowsResultSet(response, path)
