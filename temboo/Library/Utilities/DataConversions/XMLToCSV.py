# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToCSV
# Converts an XML file to CSV format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XMLToCSV(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToCSV Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XMLToCSV')


    def new_input_set(self):
        return XMLToCSVInputSet()

    def _make_result_set(self, result, path):
        return XMLToCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToCSVChoreographyExecution(session, exec_id, path)

class XMLToCSVInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToCSV
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file to convert to CSV data.)
        """
        InputSet._set_input(self, 'XML', value)
    def set_Path(self, value):
        """
        Set the value of the Path input for this Choreo. ((optional, string) If your XML is not in "/rowset/row/column_name" format, specify a path to the rows. See documentation for examples.)
        """
        InputSet._set_input(self, 'Path', value)

class XMLToCSVResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToCSV Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_CSV(self):
        """
        Retrieve the value for the "CSV" output from this Choreo execution. ((multiline) The CSV data generated from the XML input.)
        """
        return self._output.get('CSV', None)

class XMLToCSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XMLToCSVResultSet(response, path)
