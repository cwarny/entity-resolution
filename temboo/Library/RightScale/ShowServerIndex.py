# -*- coding: utf-8 -*-

###############################################################################
#
# ShowServerIndex
# Display an index of all servers in a RightScale account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ShowServerIndex(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ShowServerIndex Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/RightScale/ShowServerIndex')


    def new_input_set(self):
        return ShowServerIndexInputSet()

    def _make_result_set(self, result, path):
        return ShowServerIndexResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ShowServerIndexChoreographyExecution(session, exec_id, path)

class ShowServerIndexInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ShowServerIndex
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

class ShowServerIndexResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ShowServerIndex Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Rightscale in XML format.)
        """
        return self._output.get('Response', None)

class ShowServerIndexChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ShowServerIndexResultSet(response, path)
