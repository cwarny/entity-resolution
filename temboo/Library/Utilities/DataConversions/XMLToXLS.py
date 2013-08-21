# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToXLS
# Converts an XML file to a Base64 encoded Excel file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XMLToXLS(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToXLS Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XMLToXLS')


    def new_input_set(self):
        return XMLToXLSInputSet()

    def _make_result_set(self, result, path):
        return XMLToXLSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToXLSChoreographyExecution(session, exec_id, path)

class XMLToXLSInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToXLS
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file you want to convert to XLS format. See documentation for information on the required XML schema.)
        """
        InputSet._set_input(self, 'XML', value)

class XMLToXLSResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToXLS Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_XLS(self):
        """
        Retrieve the value for the "XLS" output from this Choreo execution. (The Base64 encoded Excel data .)
        """
        return self._output.get('XLS', None)

class XMLToXLSChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XMLToXLSResultSet(response, path)
