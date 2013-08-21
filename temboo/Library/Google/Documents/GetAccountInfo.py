# -*- coding: utf-8 -*-

###############################################################################
#
# GetAccountInfo
# Retrieves information about a specified Google Documents account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetAccountInfo(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetAccountInfo Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/GetAccountInfo')


    def new_input_set(self):
        return GetAccountInfoInputSet()

    def _make_result_set(self, result, path):
        return GetAccountInfoResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetAccountInfoChoreographyExecution(session, exec_id, path)

class GetAccountInfoInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetAccountInfo
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Google account password.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Google account username.)
        """
        InputSet._set_input(self, 'Username', value)

class GetAccountInfoResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetAccountInfo Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from the Google Documents API.)
        """
        return self._output.get('Response', None)

class GetAccountInfoChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetAccountInfoResultSet(response, path)
