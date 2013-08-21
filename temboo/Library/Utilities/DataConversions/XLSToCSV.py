# -*- coding: utf-8 -*-

###############################################################################
#
# XLSToCSV
# Converts Excel (.xls) formatted data to CSV.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XLSToCSV(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XLSToCSV Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XLSToCSV')


    def new_input_set(self):
        return XLSToCSVInputSet()

    def _make_result_set(self, result, path):
        return XLSToCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XLSToCSVChoreographyExecution(session, exec_id, path)

class XLSToCSVInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XLSToCSV
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XLS(self, value):
        """
        Set the value of the XLS input for this Choreo. ((conditional, string) The base64-encoded contents of the Excel file that you want to convert to CSV format. Compatible with Excel 97-2003.)
        """
        InputSet._set_input(self, 'XLS', value)


class XLSToCSVResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XLSToCSV Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CSV(self):
        """
        Retrieve the value for the "CSV" output from this Choreo execution. ((string) The CSV formatted data.)
        """
        return self._output.get('CSV', None)

class XLSToCSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XLSToCSVResultSet(response, path)
