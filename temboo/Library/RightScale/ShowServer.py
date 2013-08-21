# -*- coding: utf-8 -*-

###############################################################################
#
# ShowServer
# Display a comrephensive set of information about the querried server such as: state information, server templates used, SSH key href, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShowServer(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowServer Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RightScale/ShowServer')


    def new_input_set(self):
        return ShowServerInputSet()

    def _make_result_set(self, result, path):
        return ShowServerResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowServerChoreographyExecution(session, exec_id, path)

class ShowServerInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowServer
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
    def set_ServerID(self, value):
        """
        Set the value of the ServerID input for this Choreo. ((required, integer) The RightScale Server ID that is to be stopped.)
        """
        InputSet._set_input(self, 'ServerID', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) The RightScale username.)
        """
        InputSet._set_input(self, 'Username', value)

class ShowServerResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowServer Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class ShowServerChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowServerResultSet(response, path)
