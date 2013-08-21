# -*- coding: utf-8 -*-

###############################################################################
#
# HTMLEscape
# Replaces HTML markup characters in the specified text with equivalent character entity names. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HTMLEscape(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HTMLEscape Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Encoding/HTMLEscape')


    def new_input_set(self):
        return HTMLEscapeInputSet()

    def _make_result_set(self, result, path):
        return HTMLEscapeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HTMLEscapeChoreographyExecution(session, exec_id, path)

class HTMLEscapeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HTMLEscape
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_UnescapedHTML(self, value):
        """
        Set the value of the UnescapedHTML input for this Choreo. ((required, string) The HTML that needs to be escaped.)
        """
        InputSet._set_input(self, 'UnescapedHTML', value)

class HTMLEscapeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HTMLEscape Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_EscapedHTML(self):
        """
        Retrieve the value for the "EscapedHTML" output from this Choreo execution. ((string) The escaped HTML.)
        """
        return self._output.get('EscapedHTML', None)

class HTMLEscapeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HTMLEscapeResultSet(response, path)
