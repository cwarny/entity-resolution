# -*- coding: utf-8 -*-

###############################################################################
#
# TSVToJSON
# Converts a TSV formatted file to JSON.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class TSVToJSON(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the TSVToJSON Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/DataConversions/TSVToJSON')


    def new_input_set(self):
        return TSVToJSONInputSet()

    def _make_result_set(self, result, path):
        return TSVToJSONResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return TSVToJSONChoreographyExecution(session, exec_id, path)

class TSVToJSONInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the TSVToJSON
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_TSV(self, value):
        """
        Set the value of the TSV input for this Choreo. ((required, multiline) The TSV file to convert to XML. Your TSV data must contain column names.)
        """
        InputSet._set_input(self, 'TSV', value)

class TSVToJSONResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the TSVToJSON Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_JSON(self):
        """
        Retrieve the value for the "JSON" output from this Choreo execution. ((json) The JSON formatted data.)
        """
        return self._output.get('JSON', None)

class TSVToJSONChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return TSVToJSONResultSet(response, path)
