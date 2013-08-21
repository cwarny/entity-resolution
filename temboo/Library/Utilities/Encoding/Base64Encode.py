# -*- coding: utf-8 -*-

###############################################################################
#
# Base64Encode
# Returns the specified text as a Base64 encoded string.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Base64Encode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Base64Encode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Encoding/Base64Encode')


    def new_input_set(self):
        return Base64EncodeInputSet()

    def _make_result_set(self, result, path):
        return Base64EncodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return Base64EncodeChoreographyExecution(session, exec_id, path)

class Base64EncodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Base64Encode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be Base64 encoded.)
        """
        InputSet._set_input(self, 'Text', value)

class Base64EncodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Base64Encode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Base64EncodedText(self):
        """
        Retrieve the value for the "Base64EncodedText" output from this Choreo execution. ((string) The Base64 encoded text.)
        """
        return self._output.get('Base64EncodedText', None)

class Base64EncodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return Base64EncodeResultSet(response, path)
