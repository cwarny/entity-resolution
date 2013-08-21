# -*- coding: utf-8 -*-

###############################################################################
#
# JSONToXML
# Converts data from JSON format to XML format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class JSONToXML(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the JSONToXML Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/JSONToXML')


    def new_input_set(self):
        return JSONToXMLInputSet()

    def _make_result_set(self, result, path):
        return JSONToXMLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return JSONToXMLChoreographyExecution(session, exec_id, path)

class JSONToXMLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the JSONToXML
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_JSON(self, value):
        """
        Set the value of the JSON input for this Choreo. ((required, json) The JSON data that you want to convert to XML.)
        """
        InputSet._set_input(self, 'JSON', value)

class JSONToXMLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the JSONToXML Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_XML(self):
        """
        Retrieve the value for the "XML" output from this Choreo execution. ((xml) The converted data in XML format.)
        """
        return self._output.get('XML', None)

class JSONToXMLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return JSONToXMLResultSet(response, path)
