# -*- coding: utf-8 -*-

###############################################################################
#
# URLEncode
# Returns the specified text string in the application/x-www-form-urlencoded format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class URLEncode(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the URLEncode Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/Encoding/URLEncode')


    def new_input_set(self):
        return URLEncodeInputSet()

    def _make_result_set(self, result, path):
        return URLEncodeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return URLEncodeChoreographyExecution(session, exec_id, path)

class URLEncodeInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the URLEncode
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Text(self, value):
        """
        Set the value of the Text input for this Choreo. ((required, string) The text that should be URL encoded.)
        """
        InputSet._set_input(self, 'Text', value)

class URLEncodeResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the URLEncode Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_URLEncodedText(self):
        """
        Retrieve the value for the "URLEncodedText" output from this Choreo execution. ((string) The URL encoded text.)
        """
        return self._output.get('URLEncodedText', None)

class URLEncodeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return URLEncodeResultSet(response, path)
