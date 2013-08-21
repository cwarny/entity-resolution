# -*- coding: utf-8 -*-

###############################################################################
#
# URLDecode
# Removes URL encoding from the specified text string.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class URLDecode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the URLDecode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Encoding/URLDecode')


    def new_input_set(self):
        return URLDecodeInputSet()

    def _make_result_set(self, result, path):
        return URLDecodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return URLDecodeChoreographyExecution(session, exec_id, path)

class URLDecodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the URLDecode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be URL decoded.)
        """
        InputSet._set_input(self, 'Text', value)

class URLDecodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the URLDecode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_URLDecodedText(self):
        """
        Retrieve the value for the "URLDecodedText" output from this Choreo execution. ((string) The URL decoded text.)
        """
        return self._output.get('URLDecodedText', None)

class URLDecodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return URLDecodeResultSet(response, path)
