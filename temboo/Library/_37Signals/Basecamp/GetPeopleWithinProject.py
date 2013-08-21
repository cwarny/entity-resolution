# -*- coding: utf-8 -*-

###############################################################################
#
# GetPeopleWithinProject
# Retrieves all people that have access to a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetPeopleWithinProject(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPeopleWithinProject Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/GetPeopleWithinProject')


    def new_input_set(self):
        return GetPeopleWithinProjectInputSet()

    def _make_result_set(self, result, path):
        return GetPeopleWithinProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPeopleWithinProjectChoreographyExecution(session, exec_id, path)

class GetPeopleWithinProjectInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPeopleWithinProject
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The Basecamp account name for you or your company. This is the first part of your account URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Basecamp password.  You can use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProjectId(self, value):
        """
        Set the value of the ProjectId input for this Choreo. ((required, integer) The ID for the project associated with the people you want to retrieve.)
        """
        InputSet._set_input(self, 'ProjectId', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Basecamp username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class GetPeopleWithinProjectResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPeopleWithinProject Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((xml) The response from Basecamp.)
        """
        return self._output.get('Response', None)

class GetPeopleWithinProjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetPeopleWithinProjectResultSet(response, path)
