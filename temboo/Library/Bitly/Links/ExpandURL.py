# -*- coding: utf-8 -*-

###############################################################################
#
# ExpandURL
# Returns the target (long) URL given a shortened bitly URL.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ExpandURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ExpandURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bitly/Links/ExpandURL')


    def new_input_set(self):
        return ExpandURLInputSet()

    def _make_result_set(self, result, path):
        return ExpandURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ExpandURLChoreographyExecution(session, exec_id, path)

class ExpandURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ExpandURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Defaults to simple "txt" format which will just return the expanded URL. "json" and "xml" are also supported.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_ShortURL(self, value):
        """
        Set the value of the ShortURL input for this Choreo. ((required, string) One or more bitly links.)
        """
        InputSet._set_input(self, 'ShortURL', value)

class ExpandURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ExpandURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class ExpandURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ExpandURLResultSet(response, path)
