# -*- coding: utf-8 -*-

###############################################################################
#
# CSVToXML
# Converts a CSV formatted file to XML.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CSVToXML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CSVToXML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/CSVToXML')


    def new_input_set(self):
        return CSVToXMLInputSet()

    def _make_result_set(self, result, path):
        return CSVToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CSVToXMLChoreographyExecution(session, exec_id, path)

class CSVToXMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CSVToXML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_CSV(self, value):
        """
        Set the value of the CSV input for this Choreo. ((required, multiline) The CSV file to convert to XML. Your CSV data must contain column names.)
        """
        InputSet._set_input(self, 'CSV', value)

class CSVToXMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CSVToXML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_XML(self):
        """
        Retrieve the value for the "XML" output from this Choreo execution. ((xml) The XML formatted data.)
        """
        return self._output.get('XML', None)

class CSVToXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CSVToXMLResultSet(response, path)
