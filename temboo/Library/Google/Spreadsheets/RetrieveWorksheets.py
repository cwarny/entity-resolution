# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveWorksheets
# Retrieves a list of worksheets in a given Google spreadsheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveWorksheets(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveWorksheets Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveWorksheets')


    def new_input_set(self):
        return RetrieveWorksheetsInputSet()

    def _make_result_set(self, result, path):
        return RetrieveWorksheetsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveWorksheetsChoreographyExecution(session, exec_id, path)

class RetrieveWorksheetsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveWorksheets
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique for key for the spreadsheet associated with the worksheet(s) you want to retrieve. Can be retrieved from RetrieveSpreadsheets Choreo.)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google email address)
        """
        InputSet._set_input(self, 'Username', value)

class RetrieveWorksheetsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveWorksheets Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class RetrieveWorksheetsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveWorksheetsResultSet(response, path)
