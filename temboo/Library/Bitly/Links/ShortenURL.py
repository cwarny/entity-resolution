# -*- coding: utf-8 -*-

###############################################################################
#
# ShortenURL
# Returns a shortened URL for a long URL that you provide.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShortenURL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShortenURL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Bitly/Links/ShortenURL')


    def new_input_set(self):
        return ShortenURLInputSet()

    def _make_result_set(self, result, path):
        return ShortenURLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShortenURLChoreographyExecution(session, exec_id, path)

class ShortenURLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShortenURL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The oAuth access token provided by Bitly.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_LongURL(self, value):
        """
        Set the value of the LongURL input for this Choreo. ((required, string) The long url that you want to shorten.)
        """
        InputSet._set_input(self, 'LongURL', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that you want the response to be in. Defaults to simple "txt" format which will just return the shortened URL. "json" and "xml" are also supported.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class ShortenURLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShortenURL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Bitly.)
        """
        return self._output.get('Response', None)

class ShortenURLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShortenURLResultSet(response, path)
