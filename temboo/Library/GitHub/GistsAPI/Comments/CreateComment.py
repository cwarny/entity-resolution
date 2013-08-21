# -*- coding: utf-8 -*-

###############################################################################
#
# CreateComment
# Creates a comment for a specified gist.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class CreateComment(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CreateComment Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/GitHub/GistsAPI/Comments/CreateComment')


    def new_input_set(self):
        return CreateCommentInputSet()

    def _make_result_set(self, result, path):
        return CreateCommentResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateCommentChoreographyExecution(session, exec_id, path)

class CreateCommentInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CreateComment
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((required, string) The Access Token retrieved during the OAuth process.)
        """
        InputSet._set_input(self, 'AccessToken', value)
    def set_Body(self, value):
        """
        Set the value of the Body input for this Choreo. ((required, string) The text for the comment.)
        """
        InputSet._set_input(self, 'Body', value)
    def set_ID(self, value):
        """
        Set the value of the ID input for this Choreo. ((required, string) The id of the gist to comment on.)
        """
        InputSet._set_input(self, 'ID', value)

class CreateCommentResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CreateComment Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """
    		
    def getJSONFromString(self, str):
        return json.loads(str)
    
    def get_Limit(self):
        """
        Retrieve the value for the "Limit" output from this Choreo execution. ((integer) The available rate limit for your account. This is returned in the GitHub response header.)
        """
        return self._output.get('Limit', None)
    def get_Remaining(self):
        """
        Retrieve the value for the "Remaining" output from this Choreo execution. ((integer) The remaining number of API requests available to you. This is returned in the GitHub response header.)
        """
        return self._output.get('Remaining', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from GitHub.)
        """
        return self._output.get('Response', None)

class CreateCommentChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateCommentResultSet(response, path)
