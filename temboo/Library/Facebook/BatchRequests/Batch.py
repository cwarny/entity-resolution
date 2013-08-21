# -*- coding: utf-8 -*-

###############################################################################
#
# Batch
# Allows you to perform multiple graph operations in one request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class Batch(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the Batch Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/BatchRequests/Batch')


    def new_input_set(self):
        return BatchInputSet()

    def _make_result_set(self, result, path):
        return BatchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchChoreographyExecution(session, exec_id, path)

class BatchInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the Batch
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Batch(self, value):
        """
        Set the value of the Batch input for this Choreo. ((required, json) A JSON object which describes each individual operation you'd like to perform. See documentation for syntax examples.)
        """
        InputSet._set_input(self, 'Batch', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class BatchResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the Batch Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) Contains the Base64 encoded value of the image retrieved from Facebook.)
        """
        return self._output.get('Response', None)

class BatchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BatchResultSet(response, path)
