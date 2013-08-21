# -*- coding: utf-8 -*-

###############################################################################
#
# XMLToJSON
# Converts data from XML format to JSON format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class XMLToJSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the XMLToJSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/XMLToJSON')


    def new_input_set(self):
        return XMLToJSONInputSet()

    def _make_result_set(self, result, path):
        return XMLToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return XMLToJSONChoreographyExecution(session, exec_id, path)

class XMLToJSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the XMLToJSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_XML(self, value):
        """
        Set the value of the XML input for this Choreo. ((required, xml) The XML file that you want to convert to JSON format.)
        """
        InputSet._set_input(self, 'XML', value)

class XMLToJSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the XMLToJSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_JSON(self):
        """
        Retrieve the value for the "JSON" output from this Choreo execution. ((json) The converted data in JSON format.)
        """
        return self._output.get('JSON', None)

class XMLToJSONChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return XMLToJSONResultSet(response, path)
