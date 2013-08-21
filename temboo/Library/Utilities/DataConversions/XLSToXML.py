# -*- coding: utf-8 -*-

###############################################################################
#
# XLSToXML
# Converts Excel (.xls) formatted data to XML.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XLSToXML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XLSToXML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XLSToXML')


    def new_input_set(self):
        return XLSToXMLInputSet()

    def _make_result_set(self, result, path):
        return XLSToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XLSToXMLChoreographyExecution(session, exec_id, path)

class XLSToXMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XLSToXML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XLS(self, value):
        """
        Set the value of the XLS input for this Choreo. ((conditional, string) The base64-encoded contents of the Excel file that you want to convert to XML. Compatible with Excel 97-2003.)
        """
        InputSet._set_input(self, 'XLS', value)


class XLSToXMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XLSToXML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_XML(self):
        """
        Retrieve the value for the "XML" output from this Choreo execution. ((xml) The data in XML format.)
        """
        return self._output.get('XML', None)

class XLSToXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XLSToXMLResultSet(response, path)
