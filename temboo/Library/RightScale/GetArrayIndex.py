# -*- coding: utf-8 -*-

###############################################################################
#
# GetArrayIndex
# Retrieve a list of server assets grouped within a particular RightScale Array. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetArrayIndex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetArrayIndex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RightScale/GetArrayIndex')


    def new_input_set(self):
        return GetArrayIndexInputSet()

    def _make_result_set(self, result, path):
        return GetArrayIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetArrayIndexChoreographyExecution(session, exec_id, path)

class GetArrayIndexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetArrayIndex
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountID(self, value):
        """
        Set the value of the AccountID input for this Choreo. ((required, string) The RightScale Account ID.)
        """
        InputSet._set_input(self, 'AccountID', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) The RightScale account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        InputSet._set_input(self, 'Username', value)

class GetArrayIndexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetArrayIndex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class GetArrayIndexChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetArrayIndexResultSet(response, path)
