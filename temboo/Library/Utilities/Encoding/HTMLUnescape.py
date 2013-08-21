# -*- coding: utf-8 -*-

###############################################################################
#
# HTMLUnescape
# Replaces character entity names in the specified text with equivalent HTML markup characters.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class HTMLUnescape(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the HTMLUnescape Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Encoding/HTMLUnescape')


    def new_input_set(self):
        return HTMLUnescapeInputSet()

    def _make_result_set(self, result, path):
        return HTMLUnescapeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return HTMLUnescapeChoreographyExecution(session, exec_id, path)

class HTMLUnescapeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the HTMLUnescape
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_EscapedHTML(self, value):
        """
        Set the value of the EscapedHTML input for this Choreo. ((required, string) The escaped HTML that should be unescaped.)
        """
        InputSet._set_input(self, 'EscapedHTML', value)

class HTMLUnescapeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the HTMLUnescape Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_UnescapedHTML(self):
        """
        Retrieve the value for the "UnescapedHTML" output from this Choreo execution. ((string) The unescaped HTML.)
        """
        return self._output.get('UnescapedHTML', None)

class HTMLUnescapeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return HTMLUnescapeResultSet(response, path)
