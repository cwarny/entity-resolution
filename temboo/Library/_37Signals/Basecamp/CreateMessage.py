# -*- coding: utf-8 -*-

###############################################################################
#
# CreateMessage
# Creates a new message under a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CreateMessage')


    def new_input_set(self):
        return CreateMessageInputSet()

    def _make_result_set(self, result, path):
        return CreateMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateMessageChoreographyExecution(session, exec_id, path)

class CreateMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountName(self, value):
        """
        Set the value of the AccountName input for this Choreo. ((required, string) The Basecamp account name for you or your company. This is the first part of your account URL.)
        """
        InputSet._set_input(self, 'AccountName', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The body of the message you're creating.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) Your Basecamp password.  You can use the value 'X' when specifying an API Key for the Username input.)
        """
        InputSet._set_input(self, 'Password', value)
    def set_ProjectId(self, value):
        """
        Set the value of the ProjectId input for this Choreo. ((required, integer) The ID of the project that the message will be created under.)
        """
        InputSet._set_input(self, 'ProjectId', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The title of the message you'e creating.)
        """
        InputSet._set_input(self, 'Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your Basecamp username or API Key.)
        """
        InputSet._set_input(self, 'Username', value)

class CreateMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Basecamp. Note that a successful request returns a null result in this output variable.)
        """
        return self._output.get('Response', None)

class CreateMessageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateMessageResultSet(response, path)
