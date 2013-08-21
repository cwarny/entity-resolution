# -*- coding: utf-8 -*-

###############################################################################
#
# MultiQuery
# Allows you to submit multiple FQL statements and retrieve all the results you need in one request.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class MultiQuery(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the MultiQuery Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Searching/MultiQuery')


    def new_input_set(self):
        return MultiQueryInputSet()

    def _make_result_set(self, result, path):
        return MultiQueryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MultiQueryChoreographyExecution(session, exec_id, path)

class MultiQueryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the MultiQuery
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Queries(self, value):
        """
        Set the value of the Queries input for this Choreo. ((required, json) A JSON dictionary containing multiple queries to execute. See documentation for formatting examples.)
        """
        InputSet._set_input(self, 'Queries', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class MultiQueryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the MultiQuery Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class MultiQueryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MultiQueryResultSet(response, path)
