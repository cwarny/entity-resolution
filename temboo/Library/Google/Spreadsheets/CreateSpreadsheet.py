# -*- coding: utf-8 -*-

###############################################################################
#
# CreateSpreadsheet
# Creates a Google spreadsheet from a CSV file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateSpreadsheet(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateSpreadsheet Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/CreateSpreadsheet')


    def new_input_set(self):
        return CreateSpreadsheetInputSet()

    def _make_result_set(self, result, path):
        return CreateSpreadsheetResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateSpreadsheetChoreographyExecution(session, exec_id, path)

class CreateSpreadsheetInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateSpreadsheet
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UploadFile(self, value):
        """
        Set the value of the UploadFile input for this Choreo. ((conditional, multiline) The data to be written to the Google spreadsheet. Should be in CSV format. This is required unless using the VaultCSVFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        InputSet._set_input(self, 'UploadFile', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The name of the new document.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google email address)
        """
        InputSet._set_input(self, 'Username', value)


class CreateSpreadsheetResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateSpreadsheet Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) Response from Google upload)
        """
        return self._output.get('Response', None)

class CreateSpreadsheetChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateSpreadsheetResultSet(response, path)
