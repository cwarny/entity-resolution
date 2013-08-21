# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccountDetails
# Returns details about a RapidShare account in key-value pairs.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAccountDetails(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccountDetails Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/GetAccountDetails')


    def new_input_set(self):
        return GetAccountDetailsInputSet()

    def _make_result_set(self, result, path):
        return GetAccountDetailsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountDetailsChoreographyExecution(session, exec_id, path)

class GetAccountDetailsInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccountDetails
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Login(self, value):
        """
        Set the value of the Login input for this Choreo. ((required, string) Your RapidShare username)
        """
        InputSet._set_input(self, 'Login', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your RapidShare password)
        """
        InputSet._set_input(self, 'Password', value)
    def set_WithCookie(self, value):
        """
        Set the value of the WithCookie input for this Choreo. ((optional, boolean) If value "1" is specified, a cookie is returned in the response)
        """
        InputSet._set_input(self, 'WithCookie', value)
    def set_WithPublicId(self, value):
        """
        Set the value of the WithPublicId input for this Choreo. ((optional, boolean) If value "1" is specified, the public id is returned in the response)
        """
        InputSet._set_input(self, 'WithPublicId', value)

class GetAccountDetailsResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccountDetails Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((string) The response from RapidShare formatted in key / value pairs.)
        """
        return self._output.get('Response', None)

class GetAccountDetailsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountDetailsResultSet(response, path)
