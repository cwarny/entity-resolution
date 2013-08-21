# -*- coding: utf-8 -*-

###############################################################################
#
# FQL
# Allows you to use a SQL-style syntax to query data in the Graph API.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class FQL(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the FQL Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Facebook/Searching/FQL')


    def new_input_set(self):
        return FQLInputSet()

    def _make_result_set(self, result, path):
        return FQLResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return FQLChoreographyExecution(session, exec_id, path)

class FQLInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the FQL
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Conditions(self, value):
        """
        Set the value of the Conditions input for this Choreo. ((required, string) The conditions to use in the WHERE clause of the FQL statement.)
        """
        InputSet._set_input(self, 'Conditions', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((required, string) The fields to return in the response.)
        """
        InputSet._set_input(self, 'Fields', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Can be set to xml or json. Defaults to json.)
        """
        InputSet._set_input(self, 'ResponseFormat', value)
    def set_Table(self, value):
        """
        Set the value of the Table input for this Choreo. ((required, string) The table to select records from.)
        """
        InputSet._set_input(self, 'Table', value)

class FQLResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the FQL Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Facebook. Corresponds to the ResponseFormat input. Defaults to JSON.)
        """
        return self._output.get('Response', None)

class FQLChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return FQLResultSet(response, path)
