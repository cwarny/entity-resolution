# -*- coding: utf-8 -*-

###############################################################################
#
# RetrieveCellFeed
# Retrieves a list of cell names and values in a specified Google worksheet.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class RetrieveCellFeed(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the RetrieveCellFeed Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Spreadsheets/RetrieveCellFeed')


    def new_input_set(self):
        return RetrieveCellFeedInputSet()

    def _make_result_set(self, result, path):
        return RetrieveCellFeedResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RetrieveCellFeedChoreographyExecution(session, exec_id, path)

class RetrieveCellFeedInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the RetrieveCellFeed
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_SpreadsheetKey(self, value):
        """
        Set the value of the SpreadsheetKey input for this Choreo. ((required, string) The unique for key for the spreadsheet associated with the cells you want to retrieve)
        """
        InputSet._set_input(self, 'SpreadsheetKey', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google email address)
        """
        InputSet._set_input(self, 'Username', value)
    def set_WorksheetId(self, value):
        """
        Set the value of the WorksheetId input for this Choreo. ((required, string) The unique id of the worksheet associated with the cells you want to retrieve)
        """
        InputSet._set_input(self, 'WorksheetId', value)

class RetrieveCellFeedResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the RetrieveCellFeed Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Google)
        """
        return self._output.get('Response', None)

class RetrieveCellFeedChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RetrieveCellFeedResultSet(response, path)
