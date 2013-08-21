# -*- coding: utf-8 -*-

###############################################################################
#
# Delete
# Generates a HTTP DELETE request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Delete(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Delete Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Utilities/HTTP/Delete')


    def new_input_set(self):
        return DeleteInputSet()

    def _make_result_set(self, result, path):
        return DeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteChoreographyExecution(session, exec_id, path)

class DeleteInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Delete
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((optional, string) A valid password. This is used if the request required basic authentication.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_RequestHeaders(self, value):
        """
        Set the value of the RequestHeaders input for this Choreo. ((optional, json) A JSON object containing up to 10 key/value pairs that will be mapped to the HTTP request headers.)
        """
        InputSet._set_input(self, 'RequestHeaders', value)
    def set_RequestParameters(self, value):
        """
        Set the value of the RequestParameters input for this Choreo. ((optional, json) A JSON object containing up to 10 key/value pairs that will be mapped to the url string as HTTP parameters.)
        """
        InputSet._set_input(self, 'RequestParameters', value)
    def set_URL(self, value):
        """
        Set the value of the URL input for this Choreo. ((required, string) The base URL for the request (including http:// or https://).)
        """
        InputSet._set_input(self, 'URL', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((optional, string) A valid username. This is used if the request required basic authentication.)
        """
        InputSet._set_input(self, 'Username', value)

class DeleteResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Delete Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_HTTPLog(self):
        """
        Retrieve the value for the "HTTPLog" output from this Choreo execution. ((string) A log of the http request that has been generated.)
        """
        return self._output.get('HTTPLog', None)
    def get_ResponseStatusCode(self):
        """
        Retrieve the value for the "ResponseStatusCode" output from this Choreo execution. ((integer) The response status code.)
        """
        return self._output.get('ResponseStatusCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from the server.)
        """
        return self._output.get('Response', None)

class DeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteResultSet(response, path)
