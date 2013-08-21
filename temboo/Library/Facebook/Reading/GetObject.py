# -*- coding: utf-8 -*-

###############################################################################
#
# GetObject
# Retrieves retrieves the details for a Graph API object that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetObject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetObject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Reading/GetObject')


    def new_input_set(self):
        return GetObjectInputSet()

    def _make_result_set(self, result, path):
        return GetObjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetObjectChoreographyExecution(session, exec_id, path)

class GetObjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetObject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) A comma separated list of fields to return (i.e. id,name).)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_ObjectID(self, value):
        """
        Set the value of the ObjectID input for this Choreo. ((required, string) The id of a graph api object to retrieve.)
        """
        InputSet._set_input(self, 'ObjectID', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)

class GetObjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetObject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Facebook.)
        """
        return self._output.get('Response', None)

class GetObjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetObjectResultSet(response, path)
